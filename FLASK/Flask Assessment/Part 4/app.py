from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'my_secret_key'  

USERNAME = "admin"
PASSWORD = "password"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Please fill out both fields', 'error')
            return redirect(url_for('login'))

        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('admin'))
        else:
            flash('Invalid credentials', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/admin')
def admin():
    if 'logged_in' in session and session['logged_in']:
        return render_template('admin.html', logged_in=True)
    else:
        flash('You must be logged in to access the admin panel', 'error')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port = 5500)
