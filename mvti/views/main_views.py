from flask import Blueprint, render_template, redirect, url_for, g, request, session
from flask_sqlalchemy import SQLAlchemy
from mvti import db
from mvti.models import Movie, Genre, User, Weather
import json
from datetime import datetime
import os
import dotenv
import requests
import random


dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

from mvti.forms import QuestionForm
from mvti.views.auth_views import login_required

bp = Blueprint('main', __name__, url_prefix='/')


WEATHER_KEY = os.environ.get('WEATHER_KEY')
OPEN_WEATHER_KEY = os.environ.get('OPEN_WEATHER_KEY')

genre_group = {"A":["Science Fiction"], "B":["Music", "Romence"], "C":["Fantasy", "Adventure", "Animation", "Comedy"], "D": ["History", "War"], "E":["Crime", "Thriller", "Action"], "F":["Horror", "Mystery"]}


@bp.route('/')
def index():
    form = QuestionForm()
    return render_template('index.html', form=form)



# ganre_id별 장르이름 데이터 생성
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


'''
TMDB에서 추출하고 전처리시킨 json파일에서 데이터를 가져와
각 Column에 맞게 DB에 저장
 '''
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


@bp.route('/charts')
def charts():
    return render_template('charts.html')

@bp.route('/recommend')
@login_required
def recommend():
    return render_template('recommend.html')



@bp.route('/test', methods=['GET', 'POST'])
@login_required
def test():
    # 현재 시간을 가져옴
    current_time = datetime.now()

    # 날짜를 형식에 맞게 포맷팅하여 변수에 저장
    date = current_time.strftime("%Y%m%d")

    # 시간을 형식에 맞게 포맷팅하여 변수에 저장
    time = current_time.strftime("%H%M")
    
    
    # 결과 출력
    print("Formatted Date:", date)
    print("Formatted Time:", time)

    # if request.method == 'POST' and 'latitude' in request.form and 'longitude' in request.form:
    #     latitude = request.form['latitude']
    #     longitude = request.form['longitude']
    #     session['latitude'] = latitude
    #     session['longitude'] = longitude
    #     print(session.get('latitude'))
    #     print("test")



        # url = f"https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey={WEATHER_KEY}&pageNo=1&numOfRows=1&dataType=JSON&base_date={date}&base_time={time}&nx={session.get('latitude')}&ny={session.get('longitude')}"
        # res = requests.get(url, verify=False)
        # print(res.text)
    print(session.get('latitude'))
    latitude = session.get('latitude')
    longitude = session.get('longitude')
    print(latitude, longitude)


    api = f"http://api.openweathermap.org/data/2.5/weather?lang=kr&lat={latitude}&lon={longitude}&appid={OPEN_WEATHER_KEY}&units=metric"
    result = requests.get(api)
    data = json.loads(result.text)


    icon = data['weather'][0]['icon']
    weather_main = data['weather'][0]['main']
    movies_data = Movie.query.order_by(Movie.popularity.desc()).all()  # 함수를 호출하도록 수정

    if User.query.filter_by(id=g.user.id).first().age < 20:
        movies_data = Movie.query.filter_by(adult=False).order_by(Movie.popularity.desc()).all()

    else:
        movies_data = Movie.query.order_by(Movie.popularity.desc()).all()


    recommend_data = []

    if weather_main == 'Clear':
        if data['main']['temp'] > 20:
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().sunny1]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))


        elif data['main']['temp'] > 10:
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().sunny2]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))

        elif data['main']['temp'] > 0:
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().sunny3]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))
    

        else:
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().sunny4]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))

    elif weather_main == 'Clouds' or 'Atmosphere':
        if data['main']['temp'] > 20:
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().cloudy1]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))

        elif data['main']['temp'] > 10:
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().cloudy2]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))


        elif data['main']['temp'] > 0:
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().cloudy3]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))
    

        else:
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().cloudy4]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))


    elif weather_main == 'Snow':
        if data['weather'][0]['id'] == 601 or 602:
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().snowy2]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))

        else:
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().snowy1]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))

    else:
        if weather_main == 'Drizzle':
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().raining1]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))

        else:
            for genre in genre_group[Weather.query.filter_by(user_id=g.user.id).first().raining2]:
                print(genre)
                genre_movies = Genre.query.filter_by(name=genre).all()
                recommend_data.extend(genre_movies)

            recommend_data = list(set(recommend_data))


    recommend_movie = []
    for movie_list in recommend_data:
        for movie in movie_list.movies:
            recommend_movie.append(movie)


    shuffled_data = random.sample(recommend_movie, len(recommend_movie))
    for movie in shuffled_data:
        print(movie.title)

    print()
    shuffled_data = shuffled_data[:3]
    for movie in shuffled_data:
        print(movie.title)

    return render_template('test_movie.html', movie_list=movies_data, data=data, icon=icon, weather_main=weather_main, recommend_data=shuffled_data)



@bp.route('/your_route', methods=['GET', 'POST'])
def your_route():
    form = QuestionForm()
 
    if form.validate_on_submit():
        selected_answer = form.question1.data

    else:
        return redirect(url_for('main.index'))

    return render_template('test/test.html', form=form, selected_answer=selected_answer)


@bp.route('/location')
def location():
    return render_template('location.html')  


@bp.route('/sendlocation', methods=['POST'])
def sendlocation():
    if request.method == 'POST' and 'latitude' in request.form and 'longitude' in request.form:
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        session['latitude'] = latitude
        session['longitude'] = longitude

        print(session.get('latitude'), session.get('longitude'))

    if request.method == 'POST' and 'city' in request.form:
        # 도시 정보 받기
        city = request.form['city']
        session['city'] = city

        print("Received city:", city)
    else:
        temp = None

    return redirect(url_for('main.test'))