from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from mvti import db
from mvti.models import Movie, Genre, Question

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/')
def index():
    return 'question index'

@bp.route('/<int:question_id>', methods=('GET', 'POST'))
#@login_required
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/detail.html', question=question)
