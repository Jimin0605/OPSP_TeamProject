from mvti import db

movie_genre_association = db.Table(
    'movie_genre_association',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
)

# TODO: User 모델 정의

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


# TODO: 질문과 답변 모델 정의
# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question = db.Column(db.String(40), nullable=False)
#     weather = db.Column(db.String(20), nullable=False)


# class Answer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
#     weight = db.Column(db.Integer, nullable=False)
#     answer = db.Column(db.String(40), nullable=False)