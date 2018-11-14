from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField
from datetime import date


class AddForm(FlaskForm):
    title = StringField('Movie title: ')
    premiere = DateField('Premiere date (dd/mm/yyyy): ', format='%m/%d/%Y', default=date.today())
    submit = SubmitField('Add Movie')


class DelForm(FlaskForm):
    #id = IntegerField("Id number of the movie: ")
    submit = SubmitField("Remove Movie")