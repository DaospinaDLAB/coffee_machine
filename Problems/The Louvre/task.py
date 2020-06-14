class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


title = input()
artist = input()
year = input()

mona_lisa = Painting(title, artist, year)

print('"{0}" by {1} ({2}) hangs in the {3}.'.format(mona_lisa.title, mona_lisa.artist, mona_lisa.year, mona_lisa.museum))
