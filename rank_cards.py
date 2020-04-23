""" A command-line interface to rank dominion cards based on user input """

import pandas as pd


# Get cards as user input.
cards = []
done = False

while not done:

    msg = "Input card name (all lowercase, no apostrophes) and press" \
       "enter, or, enter done when done"
    print(msg)

    card = input()

    if card == "done":
        done = True
    else:
        cards.append(card)


# Load scores of all cards, and cast to dictionary.
df = pd.read_csv("data/qvist.csv")
card_to_score = {}
for card, score in df.values:

    card_to_score[card] = score

# Remove any given cards from the user that we do not have scores for.
cards = [c for c in cards if c in card_to_score.keys()]

# Score the given cards from the user.
scores = [card_to_score[c] for c in cards]

# Sort cards by their qvist scores.
sorted_cards = [card for score, card in sorted(zip(scores, cards), reverse=True)]

# Pretty output.
msg = "card ...... score\n"
for card in sorted_cards:
    score = card_to_score[card]
    msg += "{} {:.2f}\n".format(card, score)
print(msg)
