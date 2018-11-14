import os, datetime
from forms import AddForm, DelForm
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


##############################
#### SQL DATABASE SECTION ####
##############################

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

database = SQLAlchemy(app)
Migrate(app, database)


##############################
####        MODELS        ####
##############################

class Movie(database.Model):

    __tablename__ = 'movies'
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.Text)
    premiere = database.Column(database.DateTime)

    def __init__(self, title, premiere):
        self.title = title
        self.premiere = premiere

    def __repr__(self):
        return f"{self.title}"


##############################
####    VIEW FUNCTIONS    ####
##############################

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    form = AddForm()

    if form.validate_on_submit():
        title = form.title.data
        premiere = form.premiere.data

        new_movie = Movie(title, premiere)

        database.session.add(new_movie)
        database.session.commit()

        return redirect(url_for('list_movies'))

    return render_template('add.html', form=form)


@app.route('/list')
def list_movies():
    movie_list = get_movies()
    return render_template('list.html', movies=movie_list)


@app.route('/delete', methods=['GET', 'POST'])
def del_movie():
    movie_list = get_movies()
    form = DelForm()

    if form.validate_on_submit():
        movie_id = request.form.get('delete')
        #id = form.id.data
        #movie = Movie.query.get(id)

        #database.session.delete(movie)
        #database.session.commit()
        print(movie_id)
        return redirect(url_for('list_movies'))

    return render_template('delete.html', form=form, movies=movie_list)


def get_movies():
    all_movies = Movie.query.all()
    number_of_movies = 0
    movie_list = {}

    for movie in all_movies:
        movie_list[number_of_movies] = (movie.id, number_of_movies, movie.title, movie.premiere.strftime("%Y-%m-%d"))
        number_of_movies += 1

    return movie_list


if __name__ == '__main__':
    app.run(debug=True)