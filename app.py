from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def homepage():
    f = open('good.txt', 'r+', encoding='utf-8')
    txt = f.readlines()
    return render_template('index.html', goods=txt)


@app.route('/add/', methods=["POST"])
def add():
    good = request.form["good"]
    f = open('good.txt', 'a+', encoding='utf-8')
    f.write("\n" + good)
    f.close()
    return """<h1>Инвентарь пополнен</h1>
              <a href='/'> Вернуться обратно </a>
           """
