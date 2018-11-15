import datetime
from movie_site import database, Movie

database.create_all()

movie1 = Movie("jakis film", datetime.datetime.utcnow().date(), 2)
movie2 = Movie("inny film", datetime.datetime.utcnow().date(), 3)

database.session.add_all([movie1, movie2])
database.session.commit()

print(Movie.query.all())
