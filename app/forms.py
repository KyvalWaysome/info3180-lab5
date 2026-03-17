# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileRequired

class MovieForm(FlaskForm):
    title = StringField(
        'Movie Title',
        validators=[
            DataRequired(message="Please enter the movie title."),
            Length(max=100, message="Title must be less than 100 characters.")
        ]
    )
    
    description = TextAreaField(
        'Description',
        validators=[
            DataRequired(message="Please provide a brief description of the movie.")
        ]
    )
    
    poster = FileField(
        'Movie Poster',
        validators=[
            FileRequired(message="Please upload a movie poster image."),
            FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Only image files are allowed (jpg, jpeg, png, gif).')
        ]
    )
