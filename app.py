from flask import Flask, jsonify, request, Response
import json
from settings import *


app = Flask(__name__)


# @app.route('/books')
# def get_books():
#     return jsonify({'books': books})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
