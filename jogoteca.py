from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def ola():
    # return ('<h1> teste </h1>')
    return render_template('lista.html', titulo='Jogo')


app.run()
