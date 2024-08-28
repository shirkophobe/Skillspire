from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('display', user_id=new_user.id))

    return render_template('register.html')

@app.route('/display/<int:user_id>')
def display(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('display.html', user=user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port =5500)
