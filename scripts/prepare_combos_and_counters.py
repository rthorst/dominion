"""
Prepare datasets of combos and counters for use in the frontend.
"""
import os
import csv
import pandas as pd

def parse_combos_into_csv():
    """
    Read combos from text file -> well formatting CSV.
    Input: ../data/combos_and_counters/2-card-combos.txt
    Output: ../data/combos_and_counters/2-card-combos.csv
    """

    # Load data.
    in_p = os.path.join("..", "data", "combos_and_counters", 
            "2-card-combos.txt")
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
    of_p = os.path.join("..", "data", "combos_and_counters", "2-card-combos.csv")
    with open(of_p, "w", newline="") as of:

        # Write header.
        w = csv.writer(of)
        w.writerow(header)

        # Write data.
        for card1, card2 in zip(card1_, card2_):
            w.writerow([card1, card2])

def parse_counters_into_csv():
    """
    Read counters from text file -> well formatting CSV.
    Input: ../data/combos_and_counters/counters.txt
    Output: ../data/combos_and_counters/counters.csv
    """

    # Load data.
    in_p = os.path.join("..", "data", "combos_and_counters", "counters.txt")
    f = open(in_p, "r")
    combos_lines = f.readlines()
    combos_lines = [line.replace("\n", "") for line in combos_lines]

    # Split combos.
    card1_ = []
    card2_ = []
    for line in combos_lines:

        card1, card2 = line.split(" vs. ")
        card1_.append(card1)
        card2_.append(card2)

    # Write CSV.
    header = ["Card1", "Card2"]
    of_p = os.path.join("..", "data", "combos_and_counters", "counters.csv")
    with open(of_p, "w", newline="") as of:

        # Write header.
        w = csv.writer(of)
        w.writerow(header)

        # Write data.
        for card1, card2 in zip(card1_, card2_):
            w.writerow([card1, card2])


def merge_combos_and_counters():
    """
    Merge datasets of combos and counters.
    Input:
        data/combos_and_counters/2-card-combos.csv
        data/combos_and_counters/counters.csv
    Output:
        data/combos_and_counters/
        counters-and-combos.csv (card1 | card 2 | interaction_type)
    """

    # Load combos and counters independently.
    df_combos = pd.read_csv("../data/combos_and_counters/2-card-combos.csv")
    df_counters = pd.read_csv("../data/combos_and_counters/counters.csv")

    # Add an indicator column for which type of interaction is 
    # present, a combo or a counter.
    df_combos["Interaction Type"] = ["combo"] * len(df_combos)
    df_counters["Interaction Type"] = ["counter"] * len(df_counters)

    # Merge the two dataframes.
    df_merged = pd.concat([df_combos, df_counters])

    # Write output.
    df_merged.to_csv("../data/combos_and_counters/combos-and-counters.csv", index=False)

if __name__ == "__main__":
    parse_combos_into_csv()
    parse_counters_into_csv()
    merge_combos_and_counters()
