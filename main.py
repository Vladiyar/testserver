from flask import Flask, jsonify, request
from sqliter_server import SQLighter

app = Flask(__name__)
db = SQLighter('server_db.db')
client = app.test_client()

data = db.get_data()

tutorials = [
    {
        'title': 'Video #1. Intro',
        'description': 'GET, POST routes'
    },
    {
        'title': 'Video #2. More features',
        'description': 'PUT, DELETE routes'
    }
]


@app.route('/tutorials', methods=['GET'])
def get_list():
    return jsonify(tutorials)


@app.route('/data', methods=['GET'])
def get_list2():
    return jsonify(data)


# @app.route('/tutorials', motheds=['POST'])
# def update_list():
#     new_one = request.json
#     tutorials.append(new_one)
#     return jsonify(tutorials)


if __name__ == '__main__':
    app.run()
