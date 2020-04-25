'''
Front-end, should allow the user to easily input cards and see them ranked.
'''

import pandas as pd
import streamlit

# Display a page title in markdown.
title_md = """
# Rank Cards in a Dominion Board

## Which cards are in play?
"""
streamlit.markdown(title_md)

def highlight(series):
    """ helper function to provide highlighting instructions
        for a pandas series
    """
    highlighting_instructions = []
    for val in series:

        instruction = "background_color: "
        if val < 33.3:
            instruction += "lightsalmon"
        elif val < 66.6:
            instruction += "lightgoldenrodyellow"
        else:
            instruction += "palegreen"

        highlighting_instructions.append(instruction)

    return highlighting_instructions

# Load data.
df_glicko = pd.read_csv("../data/glicko_concatenated_ratings.csv")
df_combos = pd.read_csv("../data/combos-and-counters.csv")

#####
#Show cards and their ratings.
#####

# Multi-select cards.
selected_cards = streamlit.multiselect(
    label="",
    options=df_glicko["Card"] # str []
        )

# Select which cards to show to the user, showing only cards selected,
# or all cards if no cards are selected.
if len(selected_cards) > 0:
    glicko_mask = [c in selected_cards for c in df_glicko.Card]

else:
    glicko_mask = [True] * len(df_glicko)

# Create the dataframe to show to the user, sorting by score.
slc_glicko = df_glicko[glicko_mask]
slc_glicko = slc_glicko.sort_values(
        by="Score", ascending=False)

# Highlight cards.
slc_glicko = slc_glicko.style.apply(
        highlight, subset=["Score"])

# Show data and header.
streamlit.markdown("### Card Ratings")
streamlit.dataframe(slc_glicko)

#####
#Detect combinations and counters.
#####

# Keep only rows of the dataframe where both cards are in play.
combo_mask = []
for card1, card2, interaction_type in df_combos.values:

    combo_is_in_play = (card1 in selected_cards 
            and card2 in selected_cards)
    combo_mask.append(combo_is_in_play)
slc_combos = df_combos[combo_mask]

# Show data and header.
streamlit.markdown("### Combinations and Counters")
streamlit.dataframe(slc_combos)

#####
#Sidebar
#####

# About text.
about_md = """
## About:
The Qvist rankings are a yearly poll of dominion players about the strength of cards. These rankings come from the Qvist poll.

A card's score reflects how highly ranked a card is compared to other cards of the same cost. For the technically minded, the score is a percentile rank.

Some cards may be missing scores. This does not imply that a card is good or bad, simply that it cannot be scored.

Contact: Robert Thorstad, thorstadrs {at} gmail {dot} com
"""
streamlit.sidebar.markdown(about_md)
