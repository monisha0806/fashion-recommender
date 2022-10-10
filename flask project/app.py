from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/home')
def login():
    return render_template('editportfolio.html')

@app.route('/result')
def result():
print(moni)
    return render_template('editportfolio.html')


if __name__ == '__main__':
    app.run()
