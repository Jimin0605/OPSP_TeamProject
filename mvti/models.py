from mvti import db

movie_genre_association = db.Table(
    'movie_genre_association',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
)

# User 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    set_weight = db.Column(db.Boolean, default=False)

    # User와 GenreInterest 간의 일대다 관계 설정
    # genre_weights = db.relationship('Genre_weight', back_populates='user')

# Movie 모델 정의
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.String(20), nullable=True)
    popularity = db.Column(db.Float, nullable=True)
    vote_count = db.Column(db.Integer, nullable=True)
    vote_average = db.Column(db.Float, nullable=True)
    overview = db.Column(db.Text, nullable=True)
    poster_path = db.Column(db.String(255), nullable=True)
    genres = db.relationship('Genre', secondary=movie_genre_association, back_populates='movies')
    adult = db.Column(db.Boolean, nullable=True)

# Genre 모델 정의
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    movies = db.relationship('Movie', secondary=movie_genre_association, back_populates='genres')

class Genre_weight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre_weight = db.Column(db.Integer, nullable=False)


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    sunny1 = db.Column(db.String(10))
    sunny2 = db.Column(db.String(10))
    sunny3 = db.Column(db.String(10))
    sunny4 = db.Column(db.String(10))

    cloudy1 = db.Column(db.String(10))
    cloudy2 = db.Column(db.String(10))
    cloudy3 = db.Column(db.String(10))
    cloudy4 = db.Column(db.String(10))

    snowy1 = db.Column(db.String(10))
    snowy2 = db.Column(db.String(10))

    raining1 = db.Column(db.String(10))
    raining2 = db.Column(db.String(10))



# 질문 모델 정의
class Question1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(40), nullable=False)
    weather = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

class Question2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(40), nullable=False)



# class Answer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
#     weight = db.Column(db.Integer, nullable=False)
#     answer = db.Column(db.String(40), nullable=False)