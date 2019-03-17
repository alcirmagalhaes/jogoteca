from flask import Flask, render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


app = Flask(__name__)
app.secret_key = 'uma_chave_secreta'

jogo1 = Jogo('fifa 2019', 'esporte', 'play station')
jogo2 = Jogo('god of war', 'mitologia', 'play station')
jogo3 = Jogo('mortal kombat', 'luta', 'play station')
lista = [jogo1, jogo2, jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogo', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect('/login')
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST'])
def criar ():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'mestre' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ', logado com sucesso!')
        return redirect('/')
    else:
        flash('não logado , tente novamente.')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')

app.run(debug=True)
