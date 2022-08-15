import sqlite3


def get_movie_by_name(name):
    con = sqlite3.connect("netflix.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    sqlite_query = ("SELECT `title`,`country`,`release_year`,`listed_in`,`description` FROM netflix limit 1")

    result = cur.execute(sqlite_query)
    data = cur.fetchone()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return dict(data)

def convert_to_jsonify():
    for listed_in in get_movie_by_name:
        title=listed_in
    return title


def get_movie_by_year(year):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query2 = ("SELECT `title`, `release_year` FROM netflix " \
                     "WHERE release_year BETWEEN year1 AND year2 " \
                     "ORDER BY `release_year` " \
                     "LIMIT 100"\
                     "AND type='Movie'")


    result = cur.execute(sqlite_query)
    mytable = prettytable.from_db_cursor(result)
    mytable.max_width = 30

    result = cur.execute(sqlite_query2)
    data = cur.fetchone()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return data[0], data[1]



def get_movie_by_raiting(year):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query3 = ("SELECT `title`, `rating`, `description` FROM netflix " \
                     "WHERE rating == raiting_name" \
                     "ORDER BY `rating` " \
                     "LIMIT 10"\
                     "AND type='Movie'")

    result = cur.execute(sqlite_query)
    mytable = prettytable.from_db_cursor(result)
    mytable.max_width = 30

    result = cur.execute(sqlite_query2)
    data = cur.fetchone()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return data[0], data[1]

def search_by_raiting(rating_name):

    for rating in data:
        children = "G"
        family = "G", "PG", "PG-13"
        adult = "R", "NC-17"
        if rating == "rating_name":
            print(data)


"""
{{ post["content"][:50] |safe }}
"""
