from mvti import db
from mvti.models import Movie, Genre


genres_list = [
    {"Action": 28},
    {"Adventure": 12},
    {"Animation": 16},
    {"Comedy": 35},
    {"Crime": 80},
    {"Documentary": 99},
    {"Drama": 18},
    {"Family": 109751},
    {"Fantasy": 14},
    {"History": 36},
    {"Horror": 27},
    {"Music": 10402},
    {"Mystery": 9648},
    {"Romance": 10749},
    {"Science Fiction": 878}, 
    {"TV Movie": 10770}, 
    {"Thriller": 53}, 
    {"War": 10752},
    {"Western": 37}]


for genre in genres_list:
    genre = Genre(
        name=genre.keys,
        id=genre.values)
    db.session.add(genre)