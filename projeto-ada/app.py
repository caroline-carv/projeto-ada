# Importa a classe Flask e o módulo 'request' do Flask
from flask import Flask, request, jsonify

# Cria uma instância da classe Flask e atribui à variável 'app'
app = Flask(__name__)

# Classe que define as operações da calculadora
class Calculadora:
    # Método para realizar a soma de dois números
    def soma(self, a, b):
        return a + b

# Cria uma instância da classe Calculadora
calc = Calculadora()

# Define a rota padrão ('/') da aplicação para aceitar requisições GET e POST
@app.route('/', methods=['GET', 'POST'])
def calcular_soma():
    # Se a requisição for do tipo GET, retorna um formulário para inserir os números
    if request.method == 'GET':
        return '''
            <form method="POST">
                <label>Primeiro número:</label>
                <input type="number" name="num1" required><br>
                <label>Segundo número:</label>
                <input type="number" name="num2" required><br>
                <button type="submit">Calcular Soma</button>
            </form>
        '''
    # Se a requisição for do tipo POST, recebe os números do formulário, calcula a soma e retorna o resultado em formato JSON
    elif request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        resultado = calc.soma(num1, num2)
        return jsonify({"resultado": resultado})

# Verifica se o arquivo está sendo executado diretamente
if __name__ == '__main__':
    # Inicia o servidor de desenvolvimento do Flask
    app.run(debug=True)
