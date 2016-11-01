from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return '<user {}, films added: {}>'.format(self.name, self.movies)

    def add_movie(self, name, genre):
        a = Movie(name, genre, watched=False)
        self.movies.append(a)

    def delete_movie(self, n):
        self.movies = list(filter(lambda movie: movie.name != n, self.movies))

    def watched_movies(self):
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        return movies_watched

    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for mov in json_data['movies']:
            movies.append(Movie.from_json(mov))

        user.movies = movies
        return user



