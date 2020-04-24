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

            # Load data and make cosmetic adjustments for better visualization.
df = pd.read_csv("data/qvist.csv")
df.columns = ["Card", "Score"]
df["Score"] = 100 * df["Score"]

# Multi-select cards.
selected_cards = streamlit.multiselect(
    label="",
    options=df["Card"] # str []
        )

# Select which cards to show to the user, showing only cards selected,
# or all cards if no cards are selected.
if len(selected_cards) > 0:
    mask = [c in selected_cards for c in df.Card]

else:
    mask = [True] * len(df)

# Create the dataframe to show to the user, sorting by score.
slc = df[mask]
slc = slc.sort_values(by="Score", ascending=False)

# Highlight cards.
slc = slc.style.apply(highlight, subset=["Score"])

# Show data
streamlit.dataframe(slc)

# About text.
about_md = """
## About:
The Qvist rankings are a yearly poll of dominion players about the strength of cards. These rankings come from the Qvist poll.

A card's score reflects how highly ranked a card is compared to other cards of the same cost. For the technically minded, the score is a percentile rank.

Some cards may be missing scores. This does not imply that a card is good or bad, simply that it cannot be scored.

Contact: Robert Thorstad, thorstadrs {at} gmail {dot} com
"""
streamlit.sidebar.markdown(about_md)
