import media
import fresh_tomatoes
import urllib.request
import urllib.parse
from urllib.parse import urljoin
import json

tmdb_api_key = 'e70dfa434baa19e37a3fae92106bcb47'
tmdb_data_api_url = 'https://api.themoviedb.org/3/find/'
tmdb_video_api_url = 'https://api.themoviedb.org/3/movie/'
tmdb_top_movies_data_api_url = 'https://api.themoviedb.org/3/movie/top_rated'

def get_movie_data_tmdb(imdb_id): 
    tmdb_params = urllib.parse.urlencode({'external_source': 'imdb_id', 'language': 'en-US' ,'api_key': tmdb_api_key})
    #connection = urllib.request.urlopen("https://api.themoviedb.org/3/find/tt0111161?external_source=imdb_id&language=en-US&api_key=e70dfa434baa19e37a3fae92106bcb47")
    base_url = urljoin(tmdb_data_api_url, imdb_id)
    connection = urllib.request.urlopen(base_url + "?%s" % tmdb_params)
    result = connection.read().decode(connection.headers.get_content_charset())
    connection.close()
    return result

def get_movie_video_tmdb(tmdb_id):
    tmdb_params = urllib.parse.urlencode({'language': 'en-US' ,'api_key': tmdb_api_key})
    #connection = urllib.request.urlopen("https://api.themoviedb.org/3/movie/278/videos?api_key=e70dfa434baa19e37a3fae92106bcb47&language=en-US")
    base_url = urljoin(tmdb_video_api_url, tmdb_id)
    #print(base_url)
    connection = urllib.request.urlopen(base_url + "/videos?%s" % tmdb_params)
    result = connection.read().decode(connection.headers.get_content_charset())
    connection.close()
    return result    

def get_top_movies_data_tmdb():
    #https://api.themoviedb.org/3/movie/top_rated?api_key=<<api_key>>&language=en-US&page=1
    tmdb_params = urllib.parse.urlencode({'language': 'en-US' ,'api_key': tmdb_api_key, 'page':1})
    #connection = urllib.request.urlopen("https://api.themoviedb.org/3/find/tt0111161?external_source=imdb_id&language=en-US&api_key=e70dfa434baa19e37a3fae92106bcb47")
    connection = urllib.request.urlopen(tmdb_top_movies_data_api_url + "?%s" % tmdb_params)
    result = connection.read().decode(connection.headers.get_content_charset())
    connection.close()
    return result


def generate_movie_list():

        top_movies_list = get_top_movies_data_tmdb()
        movies = []
        count = 0

        #load the json to a string
        json_data = json.loads(top_movies_list)
        
        #print(json_data["results"])

        for m in json_data["results"]:
                video = get_movie_video_tmdb(str(m['id']))
                video_key = ''

                #load the video json to a string
                json_data_video = json.loads(video)

                if json_data_video['results']:
                    for v in json_data_video['results']:
#                        print(v)
                        if v['site'] == 'YouTube' and v['type'] == 'Trailer':
#                            print(v)
                            video_key = v['key']
                            break
                
                movie = media.Movie(m['title'],
                                    m['overview'],
                                    'https://image.tmdb.org/t/p/w500' + m['poster_path'],
                                    'https://www.youtube.com/watch?v=' + video_key)
                print(m)
                movies.append(movie)
                count = count + 1
                if count >= 15:
                    break;

        '''        
        shawshank_redemption_data = get_movie_data_tmdb('tt0111161')

        #load the json to a string
        json_data = json.loads(shawshank_redemption_data)

        shawshank_redemption_video = get_movie_video_tmdb(str(json_data['movie_results'][0]['id']))

        #load the video json to a string
        json_data_video = json.loads(shawshank_redemption_video)

        print(json_data['movie_results'][0]['id'])
        print(json_data['movie_results'][0]['original_title'])
        print(json_data['movie_results'][0]['overview'])
        print('https://image.tmdb.org/t/p/w500' + json_data['movie_results'][0]['poster_path'])
        print('https://www.youtube.com/watch?v=' + json_data_video['results'][0]['key'])

        shawshank_redemption_tmdb = media.Movie(json_data['movie_results'][0]['original_title'],
                                json_data['movie_results'][0]['overview'],
                                'https://image.tmdb.org/t/p/w500' + json_data['movie_results'][0]['poster_path'],
                                'https://www.youtube.com/watch?v=' + json_data_video['results'][0]['key'])

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
        '''
        return movies

movies = generate_movie_list()
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
