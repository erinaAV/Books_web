from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """Форма авторизации"""
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    """Форма регистрации"""
    user_name = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Email адрес', validators=[DataRequired(), Email()])
    password_hash = PasswordField('Пароль', validators=[DataRequired()])
    confirm = PasswordField('Повторите пароль', validators=[DataRequired()])
    accept_tos = BooleanField('Я принимаю лицензионное соглашение', validators=[DataRequired()])
    submit = SubmitField('Создать учетную запись')


class AddCarForm(FlaskForm):
    """Форма добавления автомобиля"""
    model = StringField('Название', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    power = StringField('Описание', validators=[DataRequired()])
    color = StringField('Категория', validators=[DataRequired()])
    dealer_id = SelectField('Имя автора', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Добавить книгу')


class AddDealerForm(FlaskForm):
    """Добавление дилерского центра"""
    name = StringField('Имя', validators=[DataRequired()])
    address = StringField('Описание', validators=[DataRequired()])
    submit = SubmitField('Добавить автора')


class SearchPriceForm(FlaskForm):
    """Форма поиска по цене"""
    start_price = IntegerField('Минимальная цена', validators=[DataRequired()], default=0)
    end_price = IntegerField('Максимальная цена', validators=[DataRequired()], default=5000)
    submit = SubmitField('Поиск')


class SearchDealerForm(FlaskForm):
    """Форма поиска по дилерскому центру"""
    dealer_id = SelectField('Имя автора', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Поиск')
