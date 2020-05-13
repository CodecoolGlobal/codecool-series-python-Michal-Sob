from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors():
    return data_manager.execute_select(''' SELECT id, name, birthday, death, biography
                                             FROM actors
                                            ORDER BY name ASC
                                            LIMIT 20;''')


def get_movies(id):
    return data_manager.execute_select(f'''SELECT title
                                             FROM shows
                                             LEFT JOIN show_characters
                                             ON show_characters.show_id = shows.id
                                             WHERE show_characters.actor_id = {id}
                                            ''')