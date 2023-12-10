from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, IntegerField, SelectMultipleField, widgets, validators
from wtforms.validators import DataRequired, Length, EqualTo, Email, NumberRange

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')
    ])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    age = IntegerField('사용자나이', validators=[
        NumberRange(min=0, max=150, message='올바른 나이가 아닙니다.')
    ])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    

class QuestionForm(FlaskForm):
    answer = SelectMultipleField(
        'Choose answers (select 2)',
        choices=[
            ('option1', 'Option 1'),
            ('option2', 'Option 2'),
            ('option3', 'Option 3'),
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers')
        ]
    )