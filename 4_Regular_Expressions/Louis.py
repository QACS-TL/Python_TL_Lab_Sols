import sys
import imdb
import re
def main():
    ia = imdb.IMDb()
    pattern = input("Enter movie search string: ")
    for rank, movie in enumerate(ia.get_top250_movies(), start=1):
        pattern = pattern
        if re.match(".*" + pattern + ".*", str(movie)):
            print(f"{rank:>4}: {movie}")
    return None
if __name__ == "__main__":
    main()
    sys.exit(0)