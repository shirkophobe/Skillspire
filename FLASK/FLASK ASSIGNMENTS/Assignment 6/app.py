from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'my_secret_key'  # Required for session management

@app.route('/')
def index():
    # Initialize the counter in the session if it doesn't exist
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1

    return f"Counter: {session['counter']}"

@app.route('/addtwo')
def add_two():
    if 'counter' in session:
        session['counter'] += 2
    else:
        session['counter'] = 2

    return f"Counter: {session['counter']}"

@app.route('/reset')
def reset():
    session['counter'] = 0
    return f"Counter has been reset. Current value: {session['counter']}"

if __name__ == '__main__':
    app.run(debug=True, port = 5500)