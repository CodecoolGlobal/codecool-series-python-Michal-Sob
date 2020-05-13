from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/most-rated')
def most_rated():
    top15_shows = queries.get_15_most_rated()
    print(top15_shows)
    return render_template('shows-table.html', top15_shows=top15_shows)


@app.route('/genres')
def show_genres():
    return render_template('shows-table.html')


@app.route('/tv-show/<int:tv_show_id>')
def tv_show(tv_show_id):
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
