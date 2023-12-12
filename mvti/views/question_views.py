from flask import Blueprint, render_template, redirect, url_for, flash, request, g, session
from flask_sqlalchemy import SQLAlchemy 
from mvti import db
from mvti.models import Movie, Genre, User, Weather, Genre_weight
from mvti.forms import QuestionForm, WeightForm
from mvti.views.auth_views import login_required



bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/')
def index():
    return 'question index'


@bp.route('/1', methods=('GET', 'POST'))
@login_required
def question1():
    if request.method == 'POST':
        session['user_id'] = g.user.id
        session['sunny1'] = request.form.get('question1')
        session['sunny2'] = request.form.get('question2')
        session['sunny3'] = request.form.get('question3')
        session['sunny4'] = request.form.get('question4')

        return redirect(url_for('question.question2'))

    else:
        form = QuestionForm()
        questions = [
            form.question1,
            form.question2,
            form.question3,
            form.question4
        ]
        return render_template('question/question1.html', form=form, questions=questions)
    

@bp.route('/2', methods=('GET', 'POST'))
@login_required
def question2():
    if request.method == 'POST':
        session['cloudy1'] = request.form.get('question5')
        session['cloudy2'] = request.form.get('question6')
        session['cloudy3'] = request.form.get('question7')
        session['cloudy4'] = request.form.get('question8')

        print(request.form.get('question5'))

        return redirect(url_for('question.question3'))

    else:
        form = QuestionForm()
        questions = [
            form.question5,
            form.question6,
            form.question7,
            form.question8
        ]
        return render_template('question/question2.html', form=form, questions=questions)


@bp.route('/3', methods=('GET', 'POST'))
@login_required
def question3():
    if request.method == 'POST':
        session['snowy1'] = request.form.get('question9')
        session['snowy2'] = request.form.get('question10')
        


        return redirect(url_for('question.question4'))

    else:
        form = QuestionForm()
        questions = [
            form.question9,
            form.question10
        ]
        return render_template('question/question3.html', form=form, questions=questions)


@bp.route('/4', methods=('GET', 'POST'))
@login_required
def question4():
    if request.method == 'POST':
        session['raining1'] = request.form.get('question11')
        session['raining2'] = request.form.get('question12')

        # 데이터베이스에 저장
        user_id = session.get('user_id')
        sunny1 = session.get('sunny1')
        sunny2 = session.get('sunny2')
        sunny3 = session.get('sunny3')
        sunny4 = session.get('sunny4')
        cloudy1 = session.get('cloudy1')
        cloudy2 = session.get('cloudy2')
        cloudy3 = session.get('cloudy3')
        cloudy4 = session.get('cloudy4')
        snowy1 = session.get('snowy1')
        snowy2 = session.get('snowy2')
        raining1 = session.get('raining1')
        raining2 = session.get('raining2')

        print(raining1)

        weather = Weather(
            user_id=user_id,
            sunny1=sunny1,
            sunny2=sunny2,
            sunny3=sunny3,
            sunny4=sunny4,
            cloudy1=cloudy1,
            cloudy2=cloudy2,
            cloudy3=cloudy3,
            cloudy4=cloudy4,
            snowy1=snowy1,
            snowy2=snowy2,
            raining1=raining1,
            raining2=raining2
        )
        print(weather)


        db.session.add(weather)
        db.session.commit()

        # 세션 클리어
        session.pop('question1', None)
        session.pop('question2', None)
        session.pop('question3', None)
        session.pop('question4', None)
        session.pop('question5', None)
        session.pop('question6', None)
        session.pop('question7', None)
        session.pop('question8', None)
        session.pop('question9', None)
        session.pop('question10', None)
        session.pop('question11', None)
        session.pop('question12', None)

        return redirect(url_for('question.weight'))

    else:
        form = QuestionForm()
        questions = [
            form.question11,
            form.question12
        ]
        return render_template('question/question4.html', form=form, questions=questions)

@bp.route('/weight', methods=('GET', 'POST'))
@login_required
def weight():
    form = WeightForm()

    if request.method == 'POST':
        genre_ids = [20, 12, 16, 35, 80, 99, 18, 10751, 14, 20, 27, 10402, 9648, 10749, 878, 10770, 53, 10752, 37]
        preference_fields = ['action', 'adventure', 'animation', 'comedy', 'crime', 'documentary', 'drama', 'family',
                             'fantasy', 'history', 'horror', 'music', 'mystery', 'romance', 'science_fiction', 'tv_movie',
                             'thriller', 'war', 'western']

        for genre_id, field_name in zip(genre_ids, preference_fields):
            genre_weight = Genre_weight(
                user_id=g.user.id,
                genre_id=genre_id,
                genre_weight=getattr(form, f'{field_name}_preference').data
            )

            print(f"Genre Weight - User ID: {g.user.id}, Genre ID: {genre_id}, Weight: {getattr(form, f'{field_name}_preference').data}")
            db.session.add(genre_weight)


        db.session.commit()    

        # set_weight True로 변경
        g.user.set_weight = True
        db.session.commit()



    return render_template('question/set_weights.html', form=form)


@bp.route('/test')
def recommend_test():
    return render_template('test/test.html')