import requests
import os
import bs4

def download_openings():

    # Download HTML of openings page.
    data_url = "http://councilroom.com/openings"
    html = requests.get(data_url).text

    # Save raw HTML of openings page.
    of_p = "../data/openings/openings.html"
    with open(of_p, "w") as of:
        of.write(html)

def convert_openings_to_structured_data():

    # Load the openings as a (soupified) HTML object.
    html = open("../data/openings/openings.html", "r").read()
    soup = bs4.BeautifulSoup(html)

    # List all rows in the table, which contain card names and opening scores.
    trs = soup.find_all("tr")
    START_ROW = 1
    trs = trs[START_ROW:]

    # The level is only presented for the first card belonging to a level.
    # Thus, find the indices of <trs>

if __name__ == "__main__":
    #download_openings()
    convert_openings_to_structured_data()
