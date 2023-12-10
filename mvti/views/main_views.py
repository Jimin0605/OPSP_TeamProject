from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy
from mvti import db
from mvti.models import Movie, Genre
from mvti.forms import QuestionForm
import json



bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')



@bp.route('/hello', methods=['GET', 'POST'])
def your_route():
    form = QuestionForm()

    if form.validate_on_submit():
        selected_answers = form.answer.data
        # 여기에서 선택된 답변을 처리하거나 저장할 수 있음

    return render_template('test/test.html', form=form)

def save_genre():
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


    for genre_data in genres_list:
        for name, genre_id in genre_data.items():
            genre = Genre(name=name, id=genre_id)
            db.session.add(genre)
    db.session.commit()

def save_movie_data(movie_data):
    movie = Movie(
        id=movie_data['id'],
        title=movie_data['title'],
        release_date=movie_data['release_date'],
        popularity=movie_data['popularity'],
        vote_count=movie_data['vote_count'],
        vote_average=movie_data['vote_average'],
        overview=movie_data['overview'],
        poster_path=movie_data['poster_path'],
        adult=movie_data['adult']
    )

    for genre_id in movie_data['genre_ids']:
        genre = Genre.query.get(genre_id)
        if genre:
            movie.genres.append(genre)

        db.session.add(movie)
    db.session.commit()



# 영화 데이터 추가
@bp.route('/init_db')
def init_db():
    # genre data추가
    save_genre()

    # 'movies.json' 파일에서 데잍 읽기
    with open('data/movies.json', 'r', encoding='UTF-8') as file:
        movies_data = json.load(file)

    # Movie 모델에 데이터 추가
    for movie_data in movies_data:
        save_movie_data(movie_data)

    movie = Movie.query.first()
    movie_name = movie.title
    genres = movie.genres
    movie_genres = [genre.name for genre in genres]

    return render_template('test_movie.html', movie_name=movie_name, movie_genres=movie_genres)

@bp.route('/test')
def test():
    movies_data = Movie.query.order_by(Movie.popularity.desc()).all()
    for movie in movies_data:
        print(movie.title)
        for genre in movie.genres:
            print(genre.name)

    a = 'test'
    

    return render_template('test_movie.html', movie_list=movies_data, a=a)


@bp.route('/charts')
def charts():
    return render_template('charts.html')

@bp.route('/question2')
def question2():
    return render_template('question2.html')

@bp.route('/recommend')
def recommend():
    return render_template('recommend.html')