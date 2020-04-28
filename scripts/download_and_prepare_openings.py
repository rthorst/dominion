import pandas as pd

def preprocess_openings_dataset():
    """
    Input: ../data/openings_raw.csv
    Output: ../data/openings_preprocessed.csv

    Openings_raw.csv is a very rough CSV of the 
    openings data from councilroom.com. This function
    performs various preprocessing tasks, such as 
    removing extraneous columns and renaming the
    level from "Level +8" -> 8, etc.
    """

    # Load data.
    df = pd.read_csv("../data/openings/openings_raw.csv")

    # Convert level to integer.
    # input: e.g. "Level +8" or "Level -2"
    # output: e.g. 8 or -2
    level_integers = [level_string.lstrip("Level ").replace("+", "") 
            for level_string in df.Level]
    df["Level"] = level_integers

    # Split the two cards in the opening into separate
    # columns, being careful that some openings suggest
    # NOT buying a second card, which should be reflected
    # by an empty string.
    card1s = []
    card2s = []
    for cards_string in df.Cards:

        
        # Case 1: two cards are specified. Split on "/"
        if "/" in cards_string:
            split_cards_string = cards_string.split("/")
            
            # This formulation handles a rare edge case where
            # >2 cards are possible. E.g. nomad camp, fool's
            # gold, fool's gold. Simply retain the first two
            # cards here: the rest is clear from context.
            card1 = split_cards_string[0]
            card2 = split_cards_string[1]

        # Case 2: one card is specified. Second card is ""
        else:
            card1 = cards_string
            card2 = ""

        card1 = card1.replace(" ", "")
        card2 = card2.replace(" ", "")

        card1s.append(card1)
        card2s.append(card2)

    df["Card1"] = card1s
    df["Card2"] = card2s

    # Remove extraneous columns.
    keep_cols = ["Card1", "Card2", "Level"]
    df = df[keep_cols]

    # Save preprocessed CSV.
    df.to_csv("../data/openings/openings_preprocessed.csv")

if __name__ == "__main__":
    preprocess_openings_dataset()
