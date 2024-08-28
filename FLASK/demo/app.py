from flask import Flask, render_template, request, session  
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.secret_key = 'secret'
 
@app.route('/')
 
def root():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug = True, port = 5500)