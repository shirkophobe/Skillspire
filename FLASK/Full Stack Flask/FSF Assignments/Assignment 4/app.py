from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.String(50), nullable=False, default=datetime.now().strftime('%B %dth, %Y'))

@app.route('/users')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/users/<int:user_id>')
def show(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('show.html', user=user)

@app.route('/users/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        new_user = User(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email=request.form['email'],
            created_at=datetime.now().strftime('%B %dth, %Y')
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new.html')

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit(user_id):
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('show', user_id=user_id))
    
    return render_template('edit.html', user=user)

@app.route('/users/<int:user_id>/destroy', methods=['POST'])
def destroy(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True, port=5500)
