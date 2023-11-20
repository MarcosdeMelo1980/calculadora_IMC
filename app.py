from flask import Flask, render_template, request
from calculadora_imc import calculo_IMC

app = Flask(__name__)

def classificar_IMC(resultado_IMC):
    if resultado_IMC >= 40:
        return 'Nível: obeso grau 3'
    elif 35 <= resultado_IMC < 40:
        return 'Nível: obeso grau 2'
    elif 30 <= resultado_IMC < 35:
        return 'Nível: obeso grau 1'
    elif 25 <= resultado_IMC < 30:
        return 'Nível: pré-obesidade'
    else:
        return 'Nível: peso normal'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            resultado_IMC = calculo_IMC(peso, altura)
            classificacao = classificar_IMC(resultado_IMC)
            return render_template('resultado.html', resultado_IMC=resultado_IMC, classificacao=classificacao)
        except ValueError:
            mensagem_erro = 'Por favor, insira valores numéricos para peso e altura.'
            return render_template('index.html', mensagem_erro=mensagem_erro)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
