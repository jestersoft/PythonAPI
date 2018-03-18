# https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [[1, 'item 1'], [2, 'item 2'], [3, 'item 3']]

# endpoint to show all todos
@app.route("/todo", methods=["GET"])
def get_todos():
    return jsonify(todos)

# endpoint to create new todo
@app.route("/user", methods=["POST"])
def add_todo():
    id = request.json['id']
    todo = request.json['todo']

    todo_item = Todo(id, todo)


    return jsonify(todo_item)

if __name__ == '__main__':
    app.run(debug=True)