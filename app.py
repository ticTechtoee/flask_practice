from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

# Database Setup

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Getting the data from the Form using Input Name:
        task_content = request.form['content']
        # Creating an Object of Todo Class (Model)
        new_task = Todo(content= task_content)

        try:
            # Using object to create data in the database
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Issue in saving the data'

    else:
        # To get the data from the database
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks = tasks)


@app.route('/delete/<int:id>/')
def delete(id):
    # Fetching Query
    task_to_delete = Todo.query.get_or_404(id)

    try:
        # Commiting
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error in deleting the record'


@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'error in updating data'
    else:
        return render_template('update.html', task = task)



if __name__ == "__main__":
    app.run(debug=True)