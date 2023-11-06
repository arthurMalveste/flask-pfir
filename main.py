from flask import Flask, jsonify, render_template
import os
from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import request
import datetime
from datetime import date, datetime, timezone, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Arthur_Malveste:Amm.22.01.78@localhost/portaria'
app.config['TIMEZONE'] = 'America/Sao_Paulo'  # Substitua pelo seu fuso horário
db = SQLAlchemy(app)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tabela')
def index():
    return render_template('tabela.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
