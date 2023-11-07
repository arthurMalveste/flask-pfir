from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://portaria_xgw7_user:67o65aAyM9aahzZrcEFYNpfGj9WBqORP@dpg-cl4nn3h828mc73cvtbrg-a.oregon-postgres.render.com/portaria_xgw7'
app.config['TIMEZONE'] = 'America/Sao_Paulo'  # Substitua pelo seu fuso horário
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tabela')
def tabela():
    return render_template('tabela.html')

if __name__ == '__main':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
