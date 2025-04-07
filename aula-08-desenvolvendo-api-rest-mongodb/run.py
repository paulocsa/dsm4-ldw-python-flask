# importar o flask do pacote api

from api import app


# rodando a aplicação
if __name__ == "__main__":
    app.run(host="localhost", port="5000", debug=True)
