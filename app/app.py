from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Elestio</h1>'

@app.route('/templates')
def template():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)