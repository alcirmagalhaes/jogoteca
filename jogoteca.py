from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def ola():
    lista = ['tetris', 'fifa 2019', 'god of war', 'metal gear solid']
    return render_template('lista.html', titulo='Jogo', jogos=lista)


app.run()
