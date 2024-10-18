#! /bin/python
# Name:        top250.py
# Author:      QA2.0, Donald Cameron
# Revision:    v2.5
# Description: Download the top 250 movies chosen by Letterboxd users.
"""
    Download and display online movie information.
"""
import sys
import requests
from bs4 import BeautifulSoup
import re

def main():
    base_url = "https://letterboxd.com/jack/list/official-top-250-films-with-the-most-fans/page/{}/"
    top_movies = []

    # Scrape the first 4 pages (adjust if necessary)
    for page_num in range(1, 4):  # Adjust range according to the number of pages
        url = base_url.format(page_num)
        response = requests.get(url) # Send a GET request to fetch the page content
        soup = BeautifulSoup(response.text, "html.parser")
        movie_tags = soup.find_all("li", class_="poster-container") # Find all movie containers.

        # Extract movie details
        for movie in movie_tags:
            title = movie.find('img', class_='image').get('alt')
            top_movies.append(title)

    # Display movies  - CODE TO ADDED BELOW.
    pattern = input("Enter movie search string: ")

    for rank, movie in enumerate(top_movies, start=1):
        m = re.search(pattern, str(movie), re.IGNORECASE)
        if m:
            print(f"{rank:>4}: {movie}")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
