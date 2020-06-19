# -*- coding: UTF-8 -*-
from flask import *

from jogo import Jogo
from usuario import Usuario


titulo_pagina = 'Jogoteca'

app = Flask(__name__)
app.secret_key = 'jogos'


@app.route('/autentica', methods=['POST'])
def autentica() -> str:
    with open('data/users.csv') as arquivo_usuarios:
        for line in arquivo_usuarios.readlines():
            usuario_file = line.split(';')
            usuario: Usuario = Usuario(
                id=usuario_file[0],
                nome=usuario_file[1],
                login=usuario_file[2],
                senha=usuario_file[3]
            )

            if(usuario.login == request.form['usuario']
                    and usuario.senha == request.form['senha']):
                session['usuario_logado'] = usuario.nome
                flash(f'{usuario.nome} logado com sucesso')

                return redirect(url_for(request.form["proxima"]))

    flash('Usuário ou senha incorretos', )
    return redirect(url_for('login'))


@app.route('/login')
def login() -> str:
    titulo = 'Login'

    proxima = request.args.get('proxima')
    if (proxima is None):
        proxima = 'home'

    return render_template(
        'login.html',
        titulo_pagina = titulo_pagina,
        titulo = titulo,
        proxima = proxima
    )


@app.route('/logout')
def logout() -> str:
    if ('usuario_logado' not in session or session['usuario_logado'] is None):
        flash('Sem usuário logado.')
        return redirect('/login')
    else:
        session['usuario_logado'] = None
        flash('Logout efetuado com sucesso.')
        return redirect(url_for('login'))


@app.route('/')
def home() -> str:
    if ('usuario_logado' not in session or session['usuario_logado'] is None):
        flash('Sem usuário logado.')
        return redirect(url_for('login', proxima = 'home'))
    else:
        titulo = "Jogoteca"

        return render_template(
            'index.html',
            titulo_pagina = titulo_pagina,
            titulo = titulo
        )


@app.route('/jogos/novo')
def jogo_novo() -> str:
    if ('usuario_logado' not in session or session['usuario_logado'] is None):
        flash('Sem usuário logado.')
        return redirect(url_for('login', proxima = 'jogos_novo'))
    else:
        titulo = 'Novo Jogo'

        return render_template(
            '/jogos/novoJogo.html',
            titulo_pagina = titulo_pagina,
            titulo = titulo
    )


@app.route('/jogos/novo/salvar', methods=['POST'])
def jogo_novo_salvar() -> str:
    if ('usuario_logado' not in session or session['usuario_logado'] is None):
        flash('Sem usuário logado.')
        return redirect(url_for('login', proxima='jogo_novo'))
    else:
        ano = request.form['ano']
        nome = request.form['nome']
        categoria = request.form['categoria']
        publicador = request.form['publicador']
        console = request.form['console']

        if((ano is not None and ano != '' and ano != 0)
                and (nome is not None and nome != '')
                and (categoria is not None and categoria != '')
                and (publicador is not None and publicador != '')
                and (console is not None and console != '')):
            lines: list = []
            with open('data/games.csv', 'r') as arquivo_jogos:
                lines = arquivo_jogos.readlines()

            with open('data/games.csv', 'a') as arquivo_jogos:
                if (len(lines) > 0):
                    arquivo_jogos.write(f'\n{ano};'
                                        f'{nome};'
                                        f'{categoria};'
                                        f'{publicador};'
                                        f'{console};')
                else:
                    arquivo_jogos.write(f'{ano};'
                                        f'{nome};'
                                        f'{categoria};'
                                        f'{publicador};'
                                        f'{console};')
        elif (ano is None or ano == '' or ano == 0):
            flash("Ano não preenchido")
            return redirect(url_for('jogo_novo'))
        elif (nome is None or nome == ''):
            flash("Nome não preenchido")
            return redirect(url_for('jogo_novo'))
        elif (categoria is None or categoria == ''):
            flash("Categoria não preenchida")
            return redirect(url_for('jogo_novo'))
        elif (publicador is None or publicador == ''):
            flash("Publicador não preenchido")
            return redirect(url_for('jogo_novo'))
        elif (console is None or console == ''):
            flash("Console não preenchido")
            return redirect(url_for('jogo_novo'))

        return redirect(url_for('lista_jogos'))


@app.route('/jogos')
def lista_jogos() -> str:
    if ('usuario_logado' not in session or session['usuario_logado'] is None):
        flash('Sem usuário logado.')
        return redirect(url_for('login',proxima = 'lista_jogos'))
    else:
        titulo: str = 'Jogos'
        lista_jogos_cadastrados: list = []

        with open('data/games.csv') as arquivo_jogos:
            for line in arquivo_jogos.readlines():
                jogo_arquivo = line.split(';')

                jogo: Jogo = Jogo(
                    ano=jogo_arquivo[0],
                    nome=jogo_arquivo[1],
                    categoria=jogo_arquivo[2],
                    publicador=jogo_arquivo[3],
                    console=jogo_arquivo[4]
                )

                lista_jogos_cadastrados.append(jogo)

        return render_template(
            '/jogos/listaJogos.html',
            titulo_pagina = titulo_pagina,
            titulo = titulo,
            jogos = lista_jogos_cadastrados
        )


app.run(host='0.0.0.0', port=8080, debug=True)