from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todoData = []

@app.route('/')
def index():
    return render_template("index.html", todos = todoData)

@app.route('/create-todo', methods=["POST"])
def create_todo():
    new_todo = request.form.get("new_todo")
    todoData.append(new_todo)
    print(todoData)
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