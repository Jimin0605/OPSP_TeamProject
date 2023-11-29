from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from mvti import db
from mvti.models import Movie
import json



bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return 'mvti index'


@bp.route('/hello')
def hello():
    return 'hello world'


# 영화 데이터 추가
@bp.route('/init_db')
def init_db():
    # 'movies.json' 파일에서 데잍 읽기
    with open('data/movies.json', 'r', encoding='UTF-8') as file:
        movies_data = json.load(file)

    # Movie 모델에 데이터 추가
    for movie_data in movies_data:
        movie = Movie(
            id = movie_data['id'],
            title = movie_data['title'],
            release_date = movie_data['release_date'],
            popularity = movie_data['popularity'],
            vote_count = movie_data['vote_count'],
            vote_average = movie_data['vote_average'],
            overview = movie_data['overview'],
            poster_path = movie_data['poster_path'],
            genre_ids = movie_data['genre_ids'],
            adult = movie_data['adult']
        )
        db.session.add(movie)
    db.session.commit()

    movies_data = Movie.query.order_by(Movie.popularity.desc())


    return render_template('test_movie.html', movie_list=movies_data)

@bp.route('/test')
def test():
    with open('data/movies.json', 'r', encoding='UTF-8') as file:
        movies_data = json.load(file)

    movies_data = Movie.query.order_by(Movie.popularity.desc())
    

    return render_template('test_movie.html', movie_list=movies_data)