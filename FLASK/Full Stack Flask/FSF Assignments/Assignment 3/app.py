from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_flask_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Course {self.name}>'

@app.route('/')
def index():
    courses = Course.query.order_by(Course.id).all()
    return render_template('index.html', courses=courses)

@app.route('/add', methods=['POST'])
def add_course():
    name = request.form['name']
    description = request.form['description']
    new_course = Course(name=name, description=description)
    db.session.add(new_course)
    db.session.commit()
    return redirect('/')

@app.route('/courses/destroy/<int:id>', methods=['GET', 'POST'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(course)
        db.session.commit()
        
        courses = Course.query.order_by(Course.id).all()
        for i, course in enumerate(courses, start=1):
            course.id = i
        db.session.commit()
        
        return redirect('/')
    return render_template('confirm_delete.html', course=course)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port = 5500)
