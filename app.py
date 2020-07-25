from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def init():
    return render_template('InitPage.html')


@app.route('/formação')
def form():
    return render_template('FormPage.html')


@app.route('/knowledge')
def know():
    return render_template('KnowPage.html')


if __name__ == '__main__':
    app.run(debug=True)
