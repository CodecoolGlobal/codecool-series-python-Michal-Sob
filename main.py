from flask import Flask, render_template, url_for, jsonify
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/actors')
def show_actors():
    actors = queries.get_actors()

    return render_template('actors_table.html', actors=actors)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/actor/<int:id>/movies')
def movies(id):
    actor_movies = queries.get_movies(id)

    return jsonify(actor_movies)


@app.route('/movie/<int:id>')
def movie_details(id):
    movie = queries.get_movie_details(id)

    return render_template('movie_details.html', movie=movie[0])


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
