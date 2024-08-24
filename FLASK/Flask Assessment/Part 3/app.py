from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    phone = request.form.get('phone')
    address = request.form.get('address')
    state = request.form.get('state')
    zip_code = request.form.get('zip')

    if not (firstname and lastname and phone and address and state and zip_code):
        return "Please fill out all fields.", 400

    return render_template('confirmation.html', 
                           firstname=firstname, 
                           lastname=lastname, 
                           phone=phone, 
                           address=address, 
                           state=state, 
                           zip_code=zip_code)

if __name__ == '__main__':
    app.run(debug=True, port = 5500)

