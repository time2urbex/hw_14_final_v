import json
import sqlite3
import flask

app = flask.Flask(__name__)

# Создаем sql соединение с бд

def get_value_from_db(sql):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row

        result = connection.execute(sql).fetchall()

        return result

# Задаем параметры вывода информации по назвванию


def get_value_by_title(title):
    sql = f''' select title, country, release_year, listed_in as genre, description from netflix
    where title = '{title}'
    order by release_year desc
    limit 1 '''

    result = get_value_from_db(sql)

    for item in result:
        return dict(item)

# print(get_value_by_title('9'))

# посылаем значение из адресной строки в функцию и выводим ответ в json формате


@app.get("/movie/<title>")
def view_title(title):
    result = get_value_by_title(title)
    return app.response_class(
        response=json.dumps(result,
                            ensure_ascii=False,
                            indent=4
                            ),
        status=200,
        mimetype="application/json"
    )

# Задаем параметры вывода информации по дате выхода (промежуток от и до)

@app.get("/movie/<int:year1>/to/<int:year2>")


def get_by_date(year1, year2):
    sql = f'''
    select title, release_year from netflix
    where release_year between 2019 and 2020
    limit 100
    '''

    # посылаем значение из адресной строки в функцию и выводим ответ в json формате

    result = get_value_from_db(sql)

    tmp = []
    for item in result:
        tmp.append(dict(item))

    return app.response_class(
        response=json.dumps(tmp,
                            ensure_ascii=False,
                            indent=4
                            ),
        status=200,
        mimetype="application/json"

    )

# Задаем параметры вывода информации по возрастному рейтингу

@app.get("/rating/<rating>")
def get_by_rating(rating):
    my_dict = {
        "children": ("G"),
        "family": ("G", "PG", "PG-13"),
        "adult": ("R", "NC-17")
    }

    # my_dict.get("children")

    sql = f'''
        select title, rating, description from netflix
        where rating in {my_dict.get(rating, ("G", "NC-17"))}
    '''

    # посылаем значение из адресной строки в функцию и выводим ответ в json формате

    result = get_value_from_db(sql)

    tmp = []
    for item in result:
        tmp.append(dict(item))

    return app.response_class(
        response=json.dumps(tmp, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"

    )

# Задаем параметры вывода информации по жанру


@app.get("/genre/<genre>")
def get_by_genre(genre):
    sql = f''' 
    select title, description, listed_in from netflix
    where listed_in like '%{str(genre)[1:]}%'
    '''

    # посылаем значение из адресной строки в функцию и выводим ответ в json формате

    result = get_value_from_db(sql)

    tmp = []

    for item in result:
        tmp.append(dict(item))

    return app.response_class(
        response=json.dumps(tmp,
                            ensure_ascii=False,
                            indent=4
                            ),
        status=200,
        mimetype="application/json"
    )
# Делаем запрос по двум актерам


def step_5(name1="Rose McIver", name2="Ban Lamb"):
    sql = f'''
    select * from netflix
    where "cast" like '%{name1}%' and "cast" like '%{name2}%'
    '''

    # посылаем значение из адресной строки в функцию и выводим ответ в json формате

    result = get_value_from_db(sql)

    tmp = []
    names_dict = {}

    for item in result:
        names = set(dict(item).get("cast").split(", ")) - set([name1, name2])

        for name in names:
            names_dict[name.strip()] = names_dict.get(name.strip(), 0) + 1

    print(names_dict)

    for key, value in names_dict.items():
        if value > 2:
            tmp.append(key)

        return tmp

#Делаем запрос по типу, году и жанру

def step_6(type, year, genre):
    sql = f'''
    select * from netflix
    where type = '{typ}' and
    release_year = '{year}' and
    listed_in like '%{genre}%'
    '''

    result = get_value_from_db(sql)

    tmp = []
    for item in result:
        tmp.append(dict(item))

    return json.dumps(tmp,
                      ensure_ascii=False,
                      indent=4
                      )

# Запускаем приложение
if __name__ == '__main__':
    app.run(port=8081, debug=True)

    # print(step_6(type='TV Show'))
