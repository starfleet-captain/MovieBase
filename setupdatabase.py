import datetime
from movie_site import database, Movie

database.create_all()

movie1 = Movie("jakis film", datetime.datetime.utcnow().date())
movie2 = Movie("inny film", datetime.datetime.utcnow().date())

database.session.add_all([movie1, movie2])
database.session.commit()

print(Movie.query.all())
