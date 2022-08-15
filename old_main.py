from flask import Blueprint, render_template, request, Flask, jsonify, redirect
from old_utils import *
from old_utils import get_movie_by_name
app = Flask(__name__)




@app.route("/movie/<title_name>")
def page_by_name(title_name):
    movie = get_movie_by_name(title_name)
    return jsonify(movie)
    #render_template('by_name.html', movie=movie)

#
# @app.route("/movie/<year1>/to/<year2>")
# def page_by_years(year1, year2):
#
#     movie = get_movie_by_year(year1,year2)
#     render_template('by_year.html', movie=movie)
#
# @app.route("/rating/<rating_name>")
# def get_rating(rating_name):
#
#     movie = search_by_raiting(rating_name):
#     render_template('raiting.html', movie=movie)
#


app.run(port=3033, debug=True)


""" 
def to_jsonify():
    file =
    total_posts = get_posts_all()
    logging.info("User gets all posts")
    return jsonify(total_posts)

if __name__ == '__main__':
    print(data)
"""


"""
@app.route('/bookmarks/')
def all_bookmarks():
    total_bookmarks = get_bookmarks_all()
    logging.info("User gets all bookmarks")
    if total_bookmarks:
        return render_template('bookmarks.html', total_bookmarks=total_bookmarks)
    else: return "У вас нет постов в закладках"

@app.route('/api/posts')
def all_posts():
    total_posts = get_posts_all()
    logging.info("User gets all posts")
    return jsonify(total_posts)
"""