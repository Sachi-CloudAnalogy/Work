from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, RadioField, BooleanField
from wtforms.validators import InputRequired, Length

class SignUpForm(FlaskForm):               #creating class for forms
    
    username = StringField("Username", validators=[InputRequired(), Length(max=100)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])
    id = IntegerField('Id', validators=[InputRequired()])
    gender = RadioField('Gender', choices=['Male', 'Female', 'Others'],
                      validators=[InputRequired()])
    indian = BooleanField('Indian', default='checked')
    remarks = TextAreaField('Remarks', validators=[Length(max=200)])
    submit = SubmitField("Sign Up")


# signup.html, user.html, forms.py and signup.py  --- are part of same program