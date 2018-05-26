import media
import fresh_tomatoes
import urllib.request
import urllib.parse
import json

#omdb_api_url = 'http://www.omdbapi.com/?i=tt3896198&apikey=c497f6ec'
#omdb_api_key = 'c497f6ec'

tmdb_api_key = 'e70dfa434baa19e37a3fae92106bcb47'
tmdb_data_api_url = 'https://api.themoviedb.org/3/find/tt0111161?external_source=imdb_id&language=en-US&api_key=e70dfa434baa19e37a3fae92106bcb47'
tmdb_video_api_url = 'https://api.themoviedb.org/3/movie/550/videos?api_key=e70dfa434baa19e37a3fae92106bcb47&language=en-US'

#def get_movie_data_omdb(imdb_id): 
#    omdb_params = urllib.parse.urlencode({'i': imdb_id, 'apikey': omdb_api_key})
    ##connection = urllib.request.urlopen("http://www.omdbapi.com/?i=tt0111161&apikey=c497f6ec")
#    connection = urllib.request.urlopen("http://www.omdbapi.com/?%s" % omdb_params)
#    result = connection.read().decode(connection.headers.get_content_charset())
#    connection.close()
#    return result

#shawshank_redemption_data = get_movie_data_omdb('tt0111161')

#print(json_data['Title'])
#print(json_data['Plot'])
#print(json_data['Poster'])

def get_movie_data_tmdb(imdb_id): 
    tmdb_params = urllib.parse.urlencode({'i': imdb_id, 'apikey': tmdb_api_key})
    connection = urllib.request.urlopen("https://api.themoviedb.org/3/find/tt0111161?external_source=imdb_id&language=en-US&api_key=e70dfa434baa19e37a3fae92106bcb47")
    #connection = urllib.request.urlopen("http://www.omdbapi.com/?%s" % tmdb_params)
    result = connection.read().decode(connection.headers.get_content_charset())
    connection.close()
    return result

def get_movie_video_tmdb(tmdb_id):
    tmdb_params = urllib.parse.urlencode({'i': tmdb_id, 'apikey': tmdb_api_key})
    connection = urllib.request.urlopen("https://api.themoviedb.org/3/movie/278/videos?api_key=e70dfa434baa19e37a3fae92106bcb47&language=en-US")
    #connection = urllib.request.urlopen("http://www.omdbapi.com/?%s" % tmdb_params)
    result = connection.read().decode(connection.headers.get_content_charset())
    connection.close()
    return result    

shawshank_redemption_data = get_movie_data_tmdb('tt0111161')
shawshank_redemption_video = get_movie_video_tmdb('278')

#load the json to a string
json_data = json.loads(shawshank_redemption_data)

#load the video json to a string
json_data_video = json.loads(shawshank_redemption_video)

print(json_data['movie_results'][0]['original_title'])
print(json_data['movie_results'][0]['overview'])
print('https://image.tmdb.org/t/p/w500' + json_data['movie_results'][0]['poster_path'])
print('https://www.youtube.com/watch?v=' + json_data_video['results'][0]['key'])

shawshank_redemption_tmdb = media.Movie(json_data['movie_results'][0]['original_title'],
                        json_data['movie_results'][0]['overview'],
                        'https://image.tmdb.org/t/p/w500' + json_data['movie_results'][0]['poster_path'],
                        'https://www.youtube.com/watch?v=' + json_data_video['results'][0]['key'])

#shawshank_redemption = media.Movie(json_data['Title'],
#                        json_data['Plot'],
#                        json_data['Poster'],
#                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(shawshank_redemption.storyline)

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


movies = [shawshank_redemption_tmdb, toy_story, avatar, buraaq]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
