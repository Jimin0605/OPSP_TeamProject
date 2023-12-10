from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from mvti import db
from mvti.models import Movie, Genre
from mvti.forms import QuestionForm

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/')
def index():
    return 'question index'

@bp.route('/question2', methods=('GET', 'POST'))
def question2():
    # form = QuestionForm()
    # if form.validate_on_submit():
    #     question = Question(question=form.question.data)
    #     db.session.add(question)
    #     db.session.commit()
    #     return redirect(url_for('question.detail', question_id=question.id))
    # return render_template('question2.html', form=form)
    return render_template('question2.html')

# @bp.route('/<int:question_id>', methods=('GET', 'POST'))
# #@login_required
# def detail(question_id):
#     question = Question.query.get_or_404(question_id)
#     return render_template('question/detail.html', question=question)


@bp.route('/test')
def recommend_test():
    return render_template('test/test.html')