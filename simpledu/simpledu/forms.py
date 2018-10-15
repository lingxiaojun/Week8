from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, DataRequired


class RegisterForm(FlaskForm):
    username = StringField('�û���', validators=[DataRequired(), Length(3, 24)])
    email = StringField('����', validators=[DataRequired(), Email()])
    password = PasswordField('����', validators=[DataRequired(), Length(6, 24)])
    repeat_password = PasswordField('�ظ�����', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('�ύ')


class LoginForm(FlaskForm):
    email = StringField('����', validators=[DataRequired(), Email()])
    password = PasswordField('����', validators=[DataRequired(), Length(6, 24)])
    remember_me = BooleanField('��ס��')
    submit = SubmitField('�ύ')

