from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)


@app.route('/inicio')
def ola():
    jogo1 = Jogo('fifa 2019', 'esporte', 'play station')
    jogo2 = Jogo('god of war', 'mitologia', 'play station')
    jogo3 = Jogo('mortal kombat', 'luta', 'play station')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogo', jogos=lista)


app.run()
