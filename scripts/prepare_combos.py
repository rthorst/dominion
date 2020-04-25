"""
Prepare combos dataset for use in the front-end.
"""
import os
import csv

def parse_combos_into_csv():
    """
    Read combos from text file -> well formatting CSV.
    Input: ../data/2-card-combos.txt
    Output: ../data/2-card-combos.csv
    """

    # Load data.
    in_p = os.path.join("..", "data", "2-card-combos.txt")
    f = open(in_p, "r")
    combos_lines = f.readlines()
    combos_lines = [line.replace("\n", "") for line in combos_lines]

    # Split combos.
    card1_ = []
    card2_ = []
    for line in combos_lines:

        card1, card2 = line.split("/")
        card1_.append(card1)
        card2_.append(card2)

    # Write CSV.
    header = ["Card1", "Card2"]
    of_p = os.path.join("..", "data", "2-card-combos.csv")
    with open(of_p, "w", newline="") as of:

        # Write header.
        w = csv.writer(of)
        w.writerow(header)

        # Write data.
        for card1, card2 in zip(card1_, card2_):
            w.writerow([card1, card2])

"""
Strategy: I need to check whether any of the combos is in play.

I filter the card1, card2 dataframe to rows where Card1 is in play and
Card2 is in play.

I show the combos.
"""


if __name__ == "__main__":
    parse_combos_into_csv()
