import sqlite3


def get_movie_by_name(name):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = ("SELECT `title`, `release_year` FROM netflix "
                    "WHERE release_year BETWEEN 1943 AND 1945 "
                    "AND type='Movie'")


    result = cur.execute(sqlite_query)
    data = cur.fetchone()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return data[0], data[1]


"""
{{ post["content"][:50] |safe }}
"""
