from ..LogicLayer.StoreLogic import StoreLogic
from flask import Flask

app = Flask(__name__)
config=""

@app.route('/show_all_items')
def show_all_items(email):
    return "Not Implemented"


@app.route('/shopping_cart')
def get_shopping_cart(email):
    return "Not Implemented"


@app.route('/permissible_items')
def get_permissible_items():
    return "Not Implemented"
