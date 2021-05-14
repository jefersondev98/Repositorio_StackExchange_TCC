from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm): 
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    remember = BooleanField('Lembre-se de mim')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm): 
    name = StringField('Nome e Sobrenome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Confirme Senha', validators=[DataRequired(), EqualTo('password', message="A confirmação de senha está incorreta")])
    submit = SubmitField('Registre-se')

class ProfileForm(FlaskForm): 
    name = StringField("Nome", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    current_password = PasswordField("Senha Atual", validators=[DataRequired()])
    new_password = PasswordField("Nova Senha", validators=[DataRequired()])
    repeat_new_password = PasswordField("Confirme a nova senha", validators=[DataRequired(), EqualTo('new_password')])