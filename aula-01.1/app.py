from flask import Flask, render_template  

# Criando a aplicação Flask  
# '__name__' indica que este arquivo é o ponto de entrada da aplicação  
# 'template_folder' define a pasta onde os arquivos HTML (templates) estão armazenados  
app = Flask(__name__, template_folder='views')  


# Criando a rota principal da aplicação  
@app.route('/')  # Quando o usuário acessar a URL raiz ('/'), esta função será chamada  
def home():  
    # Renderiza e retorna o arquivo 'index.html' da pasta de templates (views)  
    return render_template('index.html')  


# Criando uma rota para a página de games  
@app.route('/games')  # Quando o usuário acessar '/games', esta função será chamada  
def games():  
    # Renderiza e retorna o arquivo 'games.html' da pasta de templates (views)  
    return render_template('games.html')  


# Iniciando o servidor Flask  
if __name__ == '__main__':  # Garante que o código só execute se o arquivo for rodado diretamente  
    app.run(
        host='localhost',  # Define que o servidor roda localmente  
        port=5000,  # Define a porta onde a aplicação será acessada  
        debug=True  # Ativa o modo debug (reinicia automaticamente ao detectar mudanças e exibe erros detalhados)  
    )  
