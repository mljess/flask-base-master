from aplicacao import app
from flask import render_template
from flask import redirect
from flask import request
from models import Presenca


@app.route('/')
def index():
    
    presente = Presenca.recupera_todas()

    ## Insere opções no menu
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': True, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/presencas',
                'texto': 'Escrever presencas'})
    menu.append({'active': False,
                'href': '/jessica',
                'texto': 'Sobre Jessica'})

    ## Inserimos tudo que foi criado no dicionário context, ele será passado para a view
    context = {'titulo': 'Página principal',
            'menu': menu,
            'presente': presente,
            'jessica': jessica}

    return render_template('index.html', **context)


@app.route('/jessica')
def jessica():
        ## Insere opções no menu
    menu = []
    ## Cada opção no menu é um dicionário
    menu.append({'active': False, # active informa se a opção está ativa, e se estiver, destaca ela na página
                'href': '/', # href é o caminho que deve ser aberto pela opção
                'texto': 'Página principal'}) # texto é o texto exibido no menu para a opção
    menu.append({'active': False,
                'href': '/presencas',
                'texto': 'Escrever presencas'})
    menu.append({'active': True,
                'href': '/jessica',
                'texto': 'Sobre Jessica'})

    ## Inserimos tudo que foi criado no dicionário context, ele será passado para a view
    context = {'titulo': 'Página do Aluno',
            'menu': menu,
            'presencas': presencas,
            'jessica': jessica}

    return render_template('jessica.html', **context)


@app.route('/presencas')
def presencas():
    menu = []
    menu.append({'active': False,
                'href': '/',
                'texto': 'Página principal'})
    menu.append({'active': True,
                'href': '/presencas',
                'texto': 'Registre sua presenca'})
    menu.append({'active': False,
                'href': '/jessica',
                'texto': 'Sobre Jessica'})
    context = {'titulo': 'Registre sua presenca',
            'menu': menu,
            'jessica': jessica}
            
    return render_template('presencas.html', **context)


@app.route('/presencas/gravar', methods=['POST'])
def gravar_presencas():
    presente = Presenca(request.form['email'], request.form['presente'], request.form['resposta'], request.form['comentarios'])
    presente.gravar()
    return redirect('/')


app.run()
