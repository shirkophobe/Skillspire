from flask import Flask, render_template, request, session 
app = Flask(__name__)
app.secret_key = 'my_secret_key' 

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1

    # return f"<h3>Counter: {session['counter']}</h3>"
    return render_template("index.html")

@app.route('/addtwo')
def add_two():
    if 'counter' in session:
        session['counter'] += 2
    else:
        session['counter'] = 2

    # return f"<h3>Counter: {session['counter']}</h3>"
    return render_template("index.html")

@app.route('/reset')
def reset():
    session['counter'] = 0
    # return f"<h3>Counter has been reset to {session['counter']}</h3>"
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port = 5500)