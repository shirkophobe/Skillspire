from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory "database"
courses = []

@app.route('/')
def index():
    return render_template('index.html', courses=courses)

@app.route('/add_course', methods=['POST'])
def add_course():
    name = request.form['name']
    description = request.form['description']
    date_added = datetime.now().strftime("%b %d %Y %I:%M%p")
    if name and description:
        courses.append({
            'name': name,
            'description': description,
            'date_added': date_added
        })
    return redirect(url_for('index'))

@app.route('/courses/destroy/<int:course_id>', methods=['GET', 'POST'])
def confirm_delete(course_id):
    if course_id > len(courses) or course_id < 1:
        return redirect(url_for('index'))
    
    course_to_delete = courses[course_id - 1]  # Adjust for zero-indexing
    
    if request.method == 'POST':
        if 'confirm' in request.form:
            courses.pop(course_id - 1)  # Adjust for zero-indexing
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
    
    return render_template('confirm_delete.html', course=course_to_delete, course_id=course_id)

if __name__ == '__main__':
    app.run(debug=True, port = 5500)
