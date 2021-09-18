from collections import namedtuple

Movie = namedtuple("Movie", ["title", "director", "published"])

movie = ("12 Angry Men", "Sidney Lumet", 1957)

title, director, published = movie

print(f"Movie {movie}")
print(f"Movie Title: {title}")
print(f"Movie Director: {director}")
print(f"Movie Published: {published}")


movies = [
    ("Eternal Sunshine of the Spotless Mind", "Michel Gondry", 2004),
    ("Memento", "Christopher Nolan", 2000),
    ("Requiem for a Dream", "Darren Aronofsky", 2000),
]

print("#" * 100)
for movie in movies:
    movie_obj = Movie(*movie)
    print(f"{movie_obj.title}({movie_obj.published})")
