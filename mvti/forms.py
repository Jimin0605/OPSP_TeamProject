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
    question1 = SelectMultipleField(
        '1-1. 화창하고 20도 이상의 더운 날씨에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q1_option1', '(1) SF'),
            ('q1_option2', '(2) 음악, 로맨스'),
            ('q1_option3', '(3) 판타지, 모험, 애니메이션, 코미디'),
            ('q1_option4', '(4) 역사, 전쟁'),
            ('q1_option5', '(5) 범죄, 스릴러, 액션'),
            ('q1_option6', '(6) 공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 1'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 1')
        ]
    )

    question2 = SelectMultipleField(
        '1-2. 화창하고 10도 이상의 산책하기 좋은 날씨에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q2_option1', '(1) SF'),
            ('q2_option2', '(2) 음악, 로맨스'),
            ('q2_option3', '(3) 판타지, 모험, 애니메이션, 코미디'),
            ('q2_option4', '(4) 역사, 전쟁'),
            ('q2_option5', '(5) 범죄, 스릴러, 액션'),
            ('q2_option6', '(6) 공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )

    question3 = SelectMultipleField(
        '1-3. 화창하고 시원한 가을날씨에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q3_option1', '(1) SF'),
            ('q3_option2', '(2) 음악, 로맨스'),
            ('q3_option3', '(3) 판타지, 모험, 애니메이션, 코미디'),
            ('q3_option4', '(4) 역사, 전쟁'),
            ('q3_option5', '(5) 범죄, 스릴러, 액션'),
            ('q3_option6', '(6) 공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )

    question4 = SelectMultipleField(
        '1-4. 화창하고 추운 겨울날씨에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q4_option1', '(1) SF'),
            ('q4_option2', '(2) 음악, 로맨스'),
            ('q4_option3', '(3) 판타지, 모험, 애니메이션, 코미디'),
            ('q4_option4', '(4) 역사, 전쟁'),
            ('q4_option5', '(5) 범죄, 스릴러, 액션'),
            ('q4_option6', '(6) 공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )

    question5 = SelectMultipleField(
        '2-1. 흐리고 20도 이상의 여름날씨에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q5_option1', '(1)SF'),
            ('q5_option2', '(2)음악, 로맨스'),
            ('q5_option3', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('q5_option4', '(4)역사, 전쟁'),
            ('q5_option5', '(5)범죄, 스릴러, 액션'),
            ('q5_option6', '(6)공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )

    question6 = SelectMultipleField(
        '2-2. 흐리고 10도 이상의 산책하기 좋은 날씨에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q6_option1', '(1)SF'),
            ('q6_option2', '(2)음악, 로맨스'),
            ('q6_option3', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('q6_option4', '(4)역사, 전쟁'),
            ('q6_option5', '(5)범죄, 스릴러, 액션'),
            ('q6_option6', '(6)공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )

    question7 = SelectMultipleField(
        '2-3. 흐리고 시원한 가을날씨에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q7_option1', '(1)SF'),
            ('q7_option2', '(2)음악, 로맨스'),
            ('q7_option3', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('q7_option4', '(4)역사, 전쟁'),
            ('q7_option5', '(5)범죄, 스릴러, 액션'),
            ('q7_option6', '(6)공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )

    question8 = SelectMultipleField(
        '2-4. 흐리고 추운 겨울날씨에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q8_option1', '(1)SF'),
            ('q8_option2', '(2)음악, 로맨스'),
            ('q8_option3', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('q8_option4', '(4)역사, 전쟁'),
            ('q8_option5', '(5)범죄, 스릴러, 액션'),
            ('q8_option6', '(6)공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )

    question9 = SelectMultipleField(
        '3-1. 조금씩 잘게 내리는 가랑눈이 내리는 날에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q9_option1', '(1)SF'),
            ('q9_option2', '(2)음악, 로맨스'),
            ('q9_option3', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('q9_option4', '(4)역사, 전쟁'),
            ('q9_option5', '(5)범죄, 스릴러, 액션'),
            ('q9_option6', '(6)공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )

    question10 = SelectMultipleField(
        '3-2. 함박눈이 펑펑 내리는 날에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q10_option1', '(1)SF'),
            ('q10option2', '(2)음악, 로맨스'),
            ('q10_option3', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('q10_option4', '(4)역사, 전쟁'),
            ('q10_option5', '(5)범죄, 스릴러, 액션'),
            ('q10_option6', '(6)공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )

    question11 = SelectMultipleField(
        '4-1. 비가 후드득후드득 조금씩 내리는 날에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q11_option1', '(1)SF'),
            ('q11=option2', '(2)음악, 로맨스'),
            ('q11_option3', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('q11_option4', '(4)역사, 전쟁'),
            ('q11_option5', '(5)범죄, 스릴러, 액션'),
            ('q11_option6', '(6)공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )

    question12 = SelectMultipleField(
        '4-2. 비가 많이 내리는 날에 어떤 영화 장르를 보고 싶나요?',
        choices=[
            ('q12_option1', '(1)SF'),
            ('q12=option2', '(2)음악, 로맨스'),
            ('q12_option3', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('q12_option4', '(4)역사, 전쟁'),
            ('q12_option5', '(5)범죄, 스릴러, 액션'),
            ('q12_option6', '(6)공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )