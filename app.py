from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

db = SQLAlchemy(app)

class Todo(db.Model):
    todo = db.Column(db.String(100), unique=True, nullable=False, primary_key= True)


#finding the current app path. (Location of this file)
project_dir = os.path.dirname(os.path.abspath(__file__))

#creating the database file (bookdatabase.db) to the sqlalchemy dependency
database_file = "sqlite:///{}".format(os.path.join(project_dir, "todo.db"))

app.config["SQLALCHEMY_DATABASE_URI"]= database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

@app.route('/')
def index():
    return render_template("index.html", todos = todoData)

todoData = [] #stores data entered
update = []



@app.route('/create-todo', methods=["POST"])
def create_todo():
    new_todo = request.form.get("new_todo") #create a variable that stores form data
    todoData.append(new_todo) #appends data to an array
    print(todoData) #prints array of things to do
    return redirect(url_for("index"))

@app.route("/delete-todo/<todo_item>")
def delete(todo_item):
    todoData.remove(todo_item)

    return redirect(url_for("index"))

index_to_update = ''
@app.route('/update/<todo_item>')
def update(todo_item):

    global index_to_update
    index_to_update = todoData.index(todo_item)
    return render_template(('update.html'), todo_item = todo_item)

@app.route('/update_item', methods = ['POST'])
def update_item():
    
    if request.method == 'POST':

        new_item = request.form.get('new_item')
        todoData[index_to_update] = new_item

        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)