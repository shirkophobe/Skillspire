from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

users = [
    {'id': 1, 'first_name': 'Jimmy', 'last_name': 'Jun', 'email': 'jjun@gmail.com', 'created_at': 'June 15th, 2015'},
    {'id': 2, 'first_name': 'Andrew', 'last_name': 'Lee', 'email': 'alee@gmail.com', 'created_at': 'June 16th, 2015'},
    {'id': 3, 'first_name': 'Joy', 'last_name': 'Patel', 'email': 'jpatel@gmail.com', 'created_at': 'June 17th, 2015'},
    {'id': 4, 'first_name': 'Eduardo', 'last_name': 'Baik', 'email': 'ebaik@gmail.com', 'created_at': 'June 18th, 2015'},
]

@app.route('/users')
def index():
    return render_template('index.html', users=users)

@app.route('/users/<int:user_id>')
def show(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return render_template('show.html', user=user)
    return "User not found", 404

@app.route('/users/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        new_user = {
            'id': len(users) + 1,
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'created_at': datetime.now().strftime('%B %dth, %Y')
        }
        users.append(new_user)
        return redirect(url_for('index'))
    return render_template('new.html')

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return "User not found", 404
    
    if request.method == 'POST':
        user['first_name'] = request.form['first_name']
        user['last_name'] = request.form['last_name']
        user['email'] = request.form['email']
        return redirect(url_for('show', user_id=user_id))
    
    return render_template('edit.html', user=user)

@app.route('/users/<int:user_id>/destroy', methods=['POST'])
def destroy(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]

    for i, user in enumerate(users):
        user['id'] = i + 1

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port = 5500)
