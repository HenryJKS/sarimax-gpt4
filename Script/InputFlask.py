from flask import Flask, request, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obter os valores inseridos pelo usuário
        x_values = request.form['x_values'].split(',')
        y_values = request.form['y_values'].split(',')

        # Converter os valores para números
        try:
            x_values = [float(x) for x in x_values]
            y_values = [float(y) for y in y_values]
        except ValueError:
            # Os valores não são validos
            return render_template('index.html', error='Por favor insire valores válidos')

        # Plotar o gráfico
        plt.plot(x_values, y_values)

        # Salvar o gráfico em um objeto BytesIO
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        # Codificar a imagem em base64
        plot_url = base64.b64encode(img.getvalue()).decode()

        return render_template('index.html', plot_url=plot_url)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    # werkzeug é um servidor web para desenvolvimento
    from werkzeug.serving import run_simple

    run_simple('localhost', 5000, app)
