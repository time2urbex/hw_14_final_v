from flask import Blueprint, render_template, request, Flask, jsonify, redirect

from utils import get_movie_by_name
app = Flask(__name__)



@app.route("/movie/<title>")
def page_movies(movie_id):
    movie = get_movie_by_name(name)
    render_template('by_name.html', movie=movie)




app.run(port=3035, debug=True)

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