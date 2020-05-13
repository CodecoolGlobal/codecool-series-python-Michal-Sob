from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors():
    return data_manager.execute_select(''' SELECT name, birthday, death, biography
                                             FROM actors
                                            ORDER BY name ASC
                                            LIMIT 15;''')


def get_movies():
    return data_manager.execute_select('''SELECT shows.*
                                             FROM actors
                                             JOIN show_characters
                                             ON actors.id = show_characters.actor_id
                                             LEFT JOIN shows
                                             ON show_characters.show_id = shows.id
                                            ''')