from mvti import db

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
    genre_ids = db.Column(db.String(255), nullable=True)
    adult = db.Column(db.Boolean, nullable=True)
    
