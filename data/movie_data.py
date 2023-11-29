import json
import requests
import dotenv
import os

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

API_KEY = os.environ.get('API_KEY')
print(API_KEY)
movies = []
genres = [{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 16, "name": "Animation"}, {"id": 35, "name": "Comedy"}, {"id": 80, "name": "Crime"}, {"id": 99, "name": "Documentary"}, {"id": 18, "name": "Drama"}, {"id": 10751, "name": "Family"}, {"id": 14, "name": "Fantasy"}, {"id": 36, "name": "History"}, {"id": 27, "name": "Horror"}, {"id": 10402, "name": "Music"}, {"id": 9648, "name": "Mystery"}, {"id": 10749, "name": "Romance"}, {"id": 878, "name": "Science Fiction"}, {"id": 10770, "name": "TV Movie"}, {"id": 53, "name": "Thriller"}, {"id": 10752, "name": "War"}, {"id": 37, "name": "Western"}]

for i in range(1, 20):
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=ko-KR&page={i}&region=KR&sort_by=popularity.desc"


    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(url, headers=headers)

    data = response.json()['results']

    for result in data:
        movie = {
            "id": result['id'],
            "title": result['title'],
            "release_date": result['release_date'],
            "popularity": result['popularity'],
            "vote_count": result['vote_count'],
            "vote_average": result['vote_average'],
            "overview": result['overview'],
            "poster_path": result['poster_path'],
            "genre_ids": result['genre_ids'],
            "adult": result['adult'],
            "poster_path": result['poster_path']
        }
        movies.append(movie)

json_movies = json.dumps(movies, ensure_ascii=False, indent=4)


with open('movies.json', 'w', encoding="UTF-8") as make_file:
    json.dump(movies, make_file, indent="\t")