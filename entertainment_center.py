import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his living toys", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://youtu.be/KYz2wyBy3kc")

passengers = media.Movie("Passengers", "SOS in Space",
"https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg", "https://www.youtube.com/watch?v=7BWWWQzTpNU")

avatar = media.Movie("Avatar", "A marine in space", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://youtu.be/cRdxXPV9GNQ")

movies = [toy_story, passengers, avatar]
fresh_tomatoes.open_movies_page(movies)
