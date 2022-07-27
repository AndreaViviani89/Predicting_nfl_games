from flask import Flask, render_template

# create an instance
app = Flask(__name__)

@app.route("/") ## Decorator 
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)