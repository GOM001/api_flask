from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        #peso = request.form['peso']
        peso = 'Você é um obseso vai correr um pouquinho'
    else:
        peso = ' '

    return render_template('index.html', name=peso)

if __name__ == '__main__':
    app.run()