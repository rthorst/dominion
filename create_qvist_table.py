"""
Translate the QVIST rankings website into a sql table.
"""

import csv
import bs4
import numpy as np

def plus_minus_to_int(unknown_type_val):
    if unknown_type_val == ' - ':
        return 0
    return int(unknown_type_val)

# Find all cards.
html = open("data/qvist-table.html", "r").read()
soup = bs4.BeautifulSoup(html)
trs = soup.findAll("tr")

# Iterate through cards
breakpoints = ["Ambassador", "Remake", "Wharf", "Donate", "Scrying Pool"]
curr_set_card_names = []
all_sets_card_names = [] # list of lists. Each list is all the card names in a set.
for tr in trs:

    # Extract one "set" of cards at a time, e.g., 0-2 cost cards is a set, etc.
    try:

        # extract all tds.
        tds = tr.findAll("td")

        # get card name from td0 and remove apostrophes.
        card_name = tds[0].findAll("a")[0].get("title")
        card_name = card_name.replace("'", "")

        # if the current card is not a breakpoint, simply add it to the current set.
        if card_name not in breakpoints:
            curr_set_card_names.append(card_name)
        else: # otherwise, add cards to all_sets_card_names and empty it.
            all_sets_card_names.append(curr_set_card_names)
            curr_set_card_names = [card_name]

    except Exception as generic_exception:
    
        print(generic_exception)

# Save the results to CSV.
of_p = "data/qvist.csv"
with open(of_p, "w", newline="") as of:

    # write header.
    w = csv.writer(of)
    header = ["card", "rank"]
    w.writerow(header)

    # write cards in each set.
    for set_card_names in all_sets_card_names: # list of strings.
       
        # score all cards by rank / n cards. Highest is best.
        qvist_scores = np.arange(0, 1, 1/len(set_card_names))[::-1]
        for card_name, qvist_score in zip(set_card_names, qvist_scores):

            # lowercase card and write.
            card_name = card_name.lower()
            w.writerow([card_name, qvist_score])


