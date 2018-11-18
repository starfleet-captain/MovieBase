from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from datetime import date


class AddForm(FlaskForm):
    ratings = [('1', 'Very bad'), ('2', 'I\'ve seen worse'), ('3', 'Nothing special, but OK'),
               ('4', 'Good'), ('5', 'Excellent!')]

    title = StringField('Movie title: ')
    premiere = DateField('Premiere date (dd/mm/yyyy): ', format='%m/%d/%Y', default=date.today())
    rate = SelectField(u'Your rate:', choices=ratings)
    submit = SubmitField('Add Movie')


class DelForm(FlaskForm):
    submit = SubmitField("Remove Movie")