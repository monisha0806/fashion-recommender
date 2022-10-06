from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/home')
def login():
    return render_template('editportfolio.html')

@app.route('/fun')
def onLogin():
    print("sajjdfjhjsj")
    return render_template('editportfolio.html')


if __name__ == '__main__':
    app.run()
