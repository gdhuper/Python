import webbrowser
import urllib
import cStringIO

class Movie():
    def __init__(self, movie_title, movie_storyline, poster, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        
    #def show_poster(self):
     #  image = cStringIO.StringIO(urllib.urlopen(self.poster_image_url))
      # img = Image.open(image)
        

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
