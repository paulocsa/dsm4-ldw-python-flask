from flask import render_template, request, redirect, url_for

jogadores = []

# Definindo um dicionário com as informações do jogo
# O dicionário 'game' possui chave-valor para o título, ano e categoria do jogo
gamelist = [
    {'titulo': 'CS-GO', 'ano': 2012, 'categoria': 'FPS Online'}
]


def init_app(app):
    # Criando a rota principal da aplicação
    # Quando o usuário acessar a URL raiz ('/'), esta função será chamada

    @app.route('/')
    def home():
        # Renderiza e retorna o arquivo 'index.html' da pasta de templates (views)
        return render_template('index.html')

    # Criando uma rota para a página de games
    # Quando o usuário acessar '/games', esta função será chamada
    # Permitindo tanto os métodos 'GET' (visualização) quanto 'POST' (envio de dados)

    @app.route('/games', methods=['GET', 'POST'])
    def games():

        game = gamelist[0]

        # Definindo uma lista com os nomes dos jogadores

        # Verifica se o método da requisição é 'POST', ou seja, se o formulário foi enviado
        if request.method == 'POST':
            # Se o campo 'jogador' foi enviado no formulário, adiciona à lista de jogadores
            if request.form.get('jogador'):
                # Corrigido para chamar o método 'get' corretamente
                jogadores.append(request.form.get('jogador'))
                return redirect(url_for('games'))

        # Retorna o template 'games.html' e passa as variáveis 'game' e 'jogadores' para o HTML
        # As variáveis são utilizadas para personalizar o conteúdo no template
        return render_template('games.html', game=game, jogadores=jogadores)

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():

        if request.method == 'POST':
            form_data = request.form.to_dict()
            gamelist.append(form_data)
            return (redirect(url_for('cadgames')))
        return render_template('cadgames.html', gamelist=gamelist)
