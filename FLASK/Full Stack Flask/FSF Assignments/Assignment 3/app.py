from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'
db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        if not name or not description:
            flash('Name and description cannot be empty!')
            return redirect(url_for('index'))
        
        new_course = Course(name=name, description=description)
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for('index'))

    courses = Course.query.order_by(Course.date_added.desc()).all()
    return render_template('index.html', courses=courses)

@app.route('/courses/destroy/<int:course_id>', methods=['GET', 'POST'])
def destroy(course_id):
    course = Course.query.get_or_404(course_id)
    if request.method == 'POST':
        db.session.delete(course)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('confirm_delete.html', course=course)

if __name__ == '__main__':
    app.run(debug=True, port = 5500)
