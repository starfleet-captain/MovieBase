from movie_site import database, Movie

database.create_all()

movie1 = Movie("jakis film")
movie2 = Movie("inny film")

database.session.add_all([movie1, movie2])
database.session.commit()

print(Movie.query.all())
