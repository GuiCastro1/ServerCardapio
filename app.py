from flask import Flask, render_template, Blueprint
import sqlite3
import os 

app = Flask(__name__)

# importa e registra blueprint
from route.formAdm import admin_bp
app.register_blueprint(admin_bp)

DATABASE = 'database.db'

@app.route('/')
def home():   
    return render_template('index.html')

# Este bloco só serve localmente, ignora no Gunicorn
if __name__ == '__main__':
    app.run(debug=True)
