 #Write a class Movie with attributes title and rating using the __init__() constructor.
#Define a method to display the movie’s title and rating.
class Movie:
    title = "err"
    def __init__(self,title,rating):
        self.title=title
        self.rating = rating

    def display_movie(self):
        print(f"{self.title},{self.rating}")

    def hit_movie(self):
        if self.rating>=100:
            print("hit")
        else:
            print("not hit")
    def update_method(self,new_rarin):
        self.rating =new_rarin

a = Movie("e",78)
print(a.title)
a.display_movie()
a.rating =100
a.display_movie()
a.update_method(77)
a.display_movie()
a.hit_movie()
print(Movie.title)
