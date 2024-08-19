from flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route('/')
 
def root():
    return render_template("form.html")
 
@app.route('/formdata', methods = ['GET','POST'])
 
def formdata():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']
        
 
    return render_template("index.html",
                            first_name=first_name, 
                            last_name=last_name, 
                            email=email, 
                            address=address, 
                            city=city, 
                            state=state, 
                            zip_code=zip_code)
    
    
if __name__ == "__main__":
    app.run(debug = True, port = 5500)