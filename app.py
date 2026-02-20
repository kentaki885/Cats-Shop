#imports
from os import name

from flask import Flask, render_template,abort, request, redirect
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from scss.types import String
from sqlalchemy import Integer
from cats_desc import cats_desc_dic

#my app
app = Flask(__name__)


#Data class
class Cat():
    def __init__(self, name, price):
        self.id = name
        self.price = f"{price}$"
        self.desc = cats_desc_dic[name]

juniors = Cat("juniors", "9.99" )
bigs = Cat("bigs", "109.99")
black_juniors = Cat("black juniors", "2.99")
fisfis = Cat("fisfis", "14.99")
white = Cat("white", "4.99")
fsifis = Cat("fsifis", "7.99")

cats = [juniors, bigs, black_juniors, fisfis, white, fsifis]

#main page
@app.route('/')
def index():
    return render_template('index.html', cats=cats)


@app.route('/<cat_id>')
def cat_page(cat_id):
    # Find the cat in your list
    cat = next((c for c in cats if c.id == cat_id), None)
    if cat is None:
        abort(404)  # Cat not found
    return render_template('cat_page.html', cat=cat)


if __name__ == '__main__':
    app.run(debug=True)
