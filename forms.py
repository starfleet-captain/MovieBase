from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from datetime import date


class AddForm(FlaskForm):
    title = StringField('Movie title: ')
    premiere = DateField('Premiere date (dd/mm/yyyy): ', format='%m/%d/%Y', default=date.today())
    rate = SelectField('Your rate:', choices=[(1, 'Very bad'), (2, 'I\'ve seen worse'), (3, 'Nothing special, but OK'),
                                              (4, 'Good'), (5, 'Excellent!')])
    submit = SubmitField('Add Movie')


class DelForm(FlaskForm):
    submit = SubmitField("Remove Movie")