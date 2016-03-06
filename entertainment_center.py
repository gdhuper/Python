#import webbroswer
import urllib
import movie_website
import fresh_tomatoes

toy_story = movie_website.Movie("Toy Story", "A story of a boy and his toys that come to life",
                                "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                "http://www.youtube.com/watch?v=vwyZH85NQC4")
#print("Title: " + toy_story.title)
#print("")
#print("Story Line: " + toy_story.storyline)
#print("")

avatar = movie_website.Movie("Avatar", "A marine on an alien planet",
                                "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                                "http://www.youtube.com/watch?v=5PSNL1qE6VY")
#print("Title: " + avatar.title)
#print("")
#print("Story Line: " + avatar.storyline)
#avatar.show_trailer()
#avatar.show_poster()

school_of_rock = movie_website.Movie("School of Rock", "A movie with music and fun",
                                     "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                                     "http://www.youtube.com/watch?v=3PsUJFEBC74")

movies = [toy_story, avatar, school_of_rock]

#fresh_tomatoes.open_movies_page(movies)
#print(movie_website.Movie.VALID_R)
print(movie_website.Movie.__doc__)
print(movie_website.Movie.__name__)
print(movie_website.Movie.__module__)


