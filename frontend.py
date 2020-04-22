'''
Front-end, should allow the user to easily input cards and see them ranked.
'''

import pandas as pd
import streamlit
import numpy as np

# Helper function to highlight rows in a dataframe.
def highlight(series):

    highlighting_instructions = []
    for v in series:

        instruction = "background_color: "
        if v < 33.3:
            instruction += "lightsalmon"
        elif v < 66.6:
            instruction += "lightgoldenrodyellow"
        else:
            instruction += "palegreen"

        highlighting_instructions.append(instruction)

    return highlighting_instructions

            # Load data and make cosmetic adjustments for better visualization.
df = pd.read_csv("qvist.csv")
df.columns = ["Card", "Score"]
df["Score"] = 100 * df["Score"]

# Multi-select cards.
selected_cards = streamlit.multiselect(
    label = "Which cards are in play?",
    options = df["Card"] # str []
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
