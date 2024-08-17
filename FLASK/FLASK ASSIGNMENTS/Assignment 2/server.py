from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display-name')
def display_name():
    name = "James Browne"  
    return render_template('display_name.html', name = name)

@app.route('/display-food')
def display_food():
    favorite_food = "Thai Cuisine"  
    image_url = "pad_thai.jpg"  
    return render_template('display_food.html', favorite_food=favorite_food, image_url=image_url)

@app.route('/display-vacation')
def display_vacation():
    favorite_vacation = "Dubai"  
    image_url = "dubai.jpg"  
    return render_template('display_vacation.html', favorite_vacation=favorite_vacation, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True, port = 5500)
