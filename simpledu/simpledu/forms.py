from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import Length, Email, EqualTo, DataRequired, URL, NumberRange
from simpledu.models import db, User, Course

class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(3, 24)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password=self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise
        ValidationError('yonghumingyicuanzai')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise
        ValidationError('youxiangyijincuenzai')

class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError('youxiangweizhuce')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('mimacuowu')

class CourseForm(FlaskForm):
    name = StringField('kechenmingchen', validators=[DataRequired(), Length(5, 32)])
    description = TextAreaField('kechenjianjie', validators=[DataRequired(), Length(20, 256)])
    image_url = StringField('fengmiantupian', validators=[DataRequired(), URL()])
    author_id = IntegerField('zuozheID', validators=[DataRequired(), NumberRange(min=1, message='wuxiaodeyonghuID')])
    submit = SubmitField('tijiao')

    def validate_author_id(self, field):
        if not User.query.get(self.author_id.data):
            raise ValidationError('yonghubucuanzai')

    def create_course(self):
        course = Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self, course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

