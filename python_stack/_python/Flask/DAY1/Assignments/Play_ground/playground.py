from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def box():
    return render_template("index.html",number=3)

@app.route('/play/<num>')
def number(num):
    return render_template("index.html",number=int(num))

@app.route('/play/<num>/<color>')
def colors(num,color):
    return render_template("index.html", number=int(num),colors=color)

if __name__ == "__main__":
    app.run(debug=True)