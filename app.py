from flask import Flask,render_template, Blueprint
import sqlite3
import os 

app = Flask(__name__)

from route.formAdm import admin_bp
app.register_blueprint(admin_bp)

DATABASE = 'database.db'


@app.route('/')
def home():   
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)