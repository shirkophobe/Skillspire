from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def display_info():
    first_name = "James"
    last_name = "Browne"
    favorite_food = "Thai"
    favorite_vacation = "Dubai"

    return f"""
    First Name: {first_name}<br>
    Last Name: {last_name}<br>
    Favorite Food: {favorite_food}<br>
    Favorite Vacation Destination: {favorite_vacation}
    """
 
if __name__ == "__main__":
    app.run(debug = True, port = 5500)