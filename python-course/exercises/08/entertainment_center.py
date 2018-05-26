import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "The story of a boy and the toys which came to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://i.pinimg.com/originals/c3/2e/40/c32e40b633ff92a2d3048f5ce8570c90.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)

buraaq = media.Movie("Buraaq",
                        "Buraaq (the rise of a superhero) is about a Muslim superhero who aims to dispel myths about his religion.",
                        "http://www.splitmoonarts.com/uploads/3/7/6/7/37672673/published/2018-03-08-10-22-21-newb.png",
                        "https://www.youtube.com/watch?v=30v3KYEluyI")
#print(buraaq.storyline)
#buraaq.show_trailer()


movies = [toy_story, avatar, buraaq]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
