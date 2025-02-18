from flask import Flask, render_template
from controllers import routes

# Criando a aplicação Flask
# '__name__' indica que este arquivo é o ponto de entrada da aplicação
# 'template_folder' define a pasta onde os arquivos HTML (templates) estão armazenados
app = Flask(__name__, template_folder='views')  # representa o nome do arquivo

routes.init_app(app)


# Iniciando o servidor Flask
if __name__ == '__main__':  # Garante que o código só execute se o arquivo for rodado diretamente
    app.run(
        host='localhost',  # Define que o servidor roda localmente
        port=5000,  # Define a porta onde a aplicação será acessada
        # Ativa o modo debug (reinicia automaticamente ao detectar mudanças e exibe erros detalhados)
        debug=True
    )
