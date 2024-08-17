from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def root():
    # return render_template("index.html", first_name = "James", 
    #                        last_name = "Browne", food = "Thai", vacation = "Dubai")
    
    return render_template("part2.html")

if __name__ == "__main__":
    app.run(debug = True, port = 5500)