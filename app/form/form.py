from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class TweetForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    tweet = StringField('Tweet', validators=[DataRequired()])
    submit = SubmitField('Create Tweet')
