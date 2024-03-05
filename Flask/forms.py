from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):               #creating class for forms
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Sign Up")
