from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_hi(name):
    return f"Hi {name}"

@app.route('/repeat/<int:repeat_time>/<msg>')
def repeat(repeat_time, msg):
    message = ""
    for i in range(repeat_time):
        message += msg + "<br>"
    return message

@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry page not found Try agein"

if __name__ == "__main__":
    app.run(debug=True)