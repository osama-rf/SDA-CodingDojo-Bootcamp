from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def cheker():
    return render_template("index.html", rows=8, colum=8)

@app.route('/<int:colums>/<int:rows>')
def specific_cols_rows(colums,rows):
    return render_template("index.html", rows=rows, colums=colums)

@app.route('/<int:colums>/<int:rows>/<string:color1>/<string:color2>')
def specific_cols_rows_with_colors(colums,rows,color1,color2):
    return render_template("index.html",rows=rows, colums=colums,color1=color1,color2=color2)


if __name__ == "__main__":
    app.run(debug=True)

