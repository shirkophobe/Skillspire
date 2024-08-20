from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'my_secret_key'  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        session['address'] = request.form['address']
        session['city'] = request.form['city']
        session['state'] = request.form['state']
        session['zip_code'] = request.form['zip_code']

        return redirect(url_for('display_data'))

    return render_template('index.html')

@app.route('/display-data')
def display_data():
    return render_template(
        'display_data.html',
        first_name=session.get('first_name'),
        last_name=session.get('last_name'),
        email=session.get('email'),
        address=session.get('address'),
        city=session.get('city'),
        state=session.get('state'),
        zip_code=session.get('zip_code')
    )
    
if __name__ == "__main__":
    app.run(debug = True, port = 5500)