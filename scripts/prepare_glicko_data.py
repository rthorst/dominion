"""
Concatenate all Glicko datasets into one.
"""

import os
import pandas as pd
import numpy as np

# The Glicko data are split across individual filenames (e.g. ways, knights,
# etc. List all of those filenames
# ignore the "concatenated" file which would be an older version of the 
# output from this script.
base_p = "../data"
in_fnames = [fname for fname in os.listdir(base_p)
        if "glicko" in fname and "concatenated" not in fname]

# Load the data from all of the glicko files into two common arrays, storing
# the names and win rates of the individual cards.
card_names = []
win_rates = []

for fname in in_fnames:

    # Load data.
    p = os.path.join(base_p, fname)
    df = pd.read_csv(p)

    # Add data from this file to the arrays holding data for all sets.
    card_colname = df.columns[1]
    card_names.extend(
            list(df[card_colname].values)
            )
    win_rates.extend(
            list(df["win %"].values)
            )

# Put the resulting data in a dataframe with column names "Card" and 
# "Score"
column_names = ["Card", "Score"]
data = np.vstack([card_names, win_rates]).T
df = pd.DataFrame(data, columns=column_names)
df["Score"] = [int(score_str.rstrip(r"%")) for score_str in df.Score]
print(df.head())

# Save.
of_p = os.path.join(base_p, "glicko_concatenated_ratings.csv")
df.to_csv(of_p, index=False)
