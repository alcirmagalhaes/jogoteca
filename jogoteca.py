from flask import Flask, render_template, request


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)

jogo1 = Jogo('fifa 2019', 'esporte', 'play station')
jogo2 = Jogo('god of war', 'mitologia', 'play station')
jogo3 = Jogo('mortal kombat', 'luta', 'play station')
lista = [jogo1, jogo2, jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogo', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST'])
def criar ():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run(debug=True)
