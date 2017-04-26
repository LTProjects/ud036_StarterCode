import fresh_tomatoes
import media

#toy story movie 
toy_story = media.Movie("Toy Story", "A story of a boy and his living toys", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://youtu.be/KYz2wyBy3kc")

#passengers movie
passengers = media.Movie("Passengers", "SOS in Space",
"https://upload.wikimedia.org/wikipedia/en/8/8e/Passengers_2016_film_poster.jpg", "https://www.youtube.com/watch?v=7BWWWQzTpNU")

#avatar movie
avatar = media.Movie("Avatar", "A marine in space", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://youtu.be/cRdxXPV9GNQ")

#created an array to pass to fresh_tomatoes
movies = [toy_story, passengers, avatar]

#generate html page with all our movies
fresh_tomatoes.open_movies_page(movies)
