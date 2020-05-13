from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_actors():
    return data_manager.execute_select(''' SELECT name, birthday, death, biography
                                             FROM actors
                                            ORDER BY name ASC
                                            LIMIT 15;''')