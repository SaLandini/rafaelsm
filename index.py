from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def page_init():
    return redirect('/salandin')

@app.route('/salandin')
def init():
    return render_template("index.html")


@app.route('/formacao')
def form():
    return render_template("FormPage.html")


@app.route('/conhecimentos')
def know():
    return render_template("KnowPage.html")


if __name__ == '__main__':
    app.run(debug=True)