from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_15_most_rated():
    return data_manager.execute_select('''SELECT title, year, runtime, rating, trailer, homepage
                                            FROM shows
                                             ORDER BY rating DESC 
                                             LIMIT 15;''')

# 'SELECT %(title)s, %(release_year)s, %(runtime)s FROM shows;', variables={'title':'title', 'release_year':'year', 'runtime':'runtime'})