from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, IntegerField, SelectMultipleField, widgets, validators, RadioField
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
            ('A', '(1) SF'),
            ('B', '(2) 음악, 로맨스'),
            ('C', '(3) 판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4) 역사, 전쟁'),
            ('E', '(5) 범죄, 스릴러, 액션'),
            ('F', '(6) 공포, 미스터리')
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
            ('A', '(1) SF'),
            ('B', '(2) 음악, 로맨스'),
            ('C', '(3) 판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4) 역사, 전쟁'),
            ('E', '(5) 범죄, 스릴러, 액션'),
            ('F', '(6) 공포, 미스터리')
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
            ('A', '(1) SF'),
            ('B', '(2) 음악, 로맨스'),
            ('C', '(3) 판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4) 역사, 전쟁'),
            ('E', '(5) 범죄, 스릴러, 액션'),
            ('F', '(6) 공포, 미스터리')
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
            ('A', '(1) SF'),
            ('B', '(2) 음악, 로맨스'),
            ('C', '(3) 판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4) 역사, 전쟁'),
            ('E', '(5) 범죄, 스릴러, 액션'),
            ('F', '(6) 공포, 미스터리')
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
            ('A', '(1)SF'),
            ('B', '(2)음악, 로맨스'),
            ('C', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4)역사, 전쟁'),
            ('E', '(5)범죄, 스릴러, 액션'),
            ('F', '(6)공포, 미스터리')
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
            ('A', '(1)SF'),
            ('B', '(2)음악, 로맨스'),
            ('C', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4)역사, 전쟁'),
            ('E', '(5)범죄, 스릴러, 액션'),
            ('F', '(6)공포, 미스터리')
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
            ('A', '(1)SF'),
            ('B', '(2)음악, 로맨스'),
            ('C', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4)역사, 전쟁'),
            ('E', '(5)범죄, 스릴러, 액션'),
            ('F', '(6)공포, 미스터리')
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
            ('A', '(1)SF'),
            ('B', '(2)음악, 로맨스'),
            ('C', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4)역사, 전쟁'),
            ('E', '(5)범죄, 스릴러, 액션'),
            ('F', '(6)공포, 미스터리')
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
            ('A', '(1)SF'),
            ('B', '(2)음악, 로맨스'),
            ('C', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4)역사, 전쟁'),
            ('E', '(5)범죄, 스릴러, 액션'),
            ('F', '(6)공포, 미스터리')
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
            ('A', '(1)SF'),
            ('B', '(2)음악, 로맨스'),
            ('C', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4)역사, 전쟁'),
            ('E', '(5)범죄, 스릴러, 액션'),
            ('F', '(6)공포, 미스터리')
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
            ('A', '(1)SF'),
            ('B', '(2)음악, 로맨스'),
            ('C', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4)역사, 전쟁'),
            ('E', '(5)범죄, 스릴러, 액션'),
            ('F', '(6)공포, 미스터리')
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
            ('A', '(1)SF'),
            ('B', '(2)음악, 로맨스'),
            ('C', '(3)판타지, 모험, 애니메이션, 코미디'),
            ('D', '(4)역사, 전쟁'),
            ('E', '(5)범죄, 스릴러, 액션'),
            ('F', '(6)공포, 미스터리')
            # Add more options as needed
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        validators=[
            validators.InputRequired(message='Please choose at least one answer for Question 2'),
            validators.Length(min=2, max=2, message='Please choose exactly 2 answers for Question 2')
        ]
    )


class WeightForm(FlaskForm):
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
        {"Western": 37}
    ]

    # genres_list에서 이름만 추출하여 튜플로 만들기
    genre_choices = [(name, name) for genre_data in genres_list for name, genre_id in genre_data.items()]

    # 선택지에 대한 값을 정의
    preference_choices = [
        (1, '전혀 즐겨보지 않음'),
        (2, '즐겨보지 않음'),
        (3, '보통'),
        (4, '즐겨봄'),
        (5, '매우 즐겨봄')
    ]

    # 각 장르에 대한 RadioField 정의
    action_preference = RadioField('Action', choices=preference_choices, validators=[])
    adventure_preference = RadioField('Adventure', choices=preference_choices, validators=[])
    animation_preference = RadioField('Animation', choices=preference_choices, validators=[])
    comedy_preference = RadioField('Comedy', choices=preference_choices, validators=[])
    crime_preference = RadioField('Crime', choices=preference_choices, validators=[])
    documentary_preference = RadioField('Documentary', choices=preference_choices, validators=[])
    drama_preference = RadioField('Drama', choices=preference_choices, validators=[])
    family_preference = RadioField('Family', choices=preference_choices, validators=[])
    fantasy_preference = RadioField('Fantasy', choices=preference_choices, validators=[])
    history_preference = RadioField('History', choices=preference_choices, validators=[])
    horror_preference = RadioField('Horror', choices=preference_choices, validators=[])
    music_preference = RadioField('Music', choices=preference_choices, validators=[])
    mystery_preference = RadioField('Mystery', choices=preference_choices, validators=[])
    romance_preference = RadioField('Romance', choices=preference_choices, validators=[])
    science_fiction_preference = RadioField('Science Fiction', choices=preference_choices, validators=[])
    tv_movie_preference = RadioField('TV Movie', choices=preference_choices, validators=[])
    thriller_preference = RadioField('Thriller', choices=preference_choices, validators=[])
    war_preference = RadioField('War', choices=preference_choices, validators=[])
    western_preference = RadioField('Western', choices=preference_choices, validators=[])
