from flask import Flask, jsonify, render_template
import os
from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import request
import datetime
from datetime import date, datetime, timezone, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://portaria_xgw7_user:67o65aAyM9aahzZrcEFYNpfGj9WBqORP@dpg-cl4nn3h828mc73cvtbrg-a.oregon-postgres.render.com/portaria_xgw7'
app.config['TIMEZONE'] = 'America/Sao_Paulo'  # Substitua pelo seu fuso horário
db = SQLAlchemy(app)




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tabela')
def index():
    return render_template('tabela.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
