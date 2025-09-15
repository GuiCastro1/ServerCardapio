import os 

from flask import Flask, render_template
from flask_cors import CORS

from models.cardapio import db

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'fallback_secreto_local')

# CORS(app)


CORS(app, resources={r"/api/*": {"origins": "https://guicastro1.github.io"}}, supports_credentials=True)


app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(app.instance_path, 'cardapio.db')}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

from route.create import create_bp
# from route.read import read_bp
# from route.update import update_bp
# from route.delete import delete_bp
from route.api import api_client_bp

app.register_blueprint(create_bp)
# app.register_blueprint(read_bp)
# app.register_blueprint(update_bp)
# app.register_blueprint(delete_bp)
app.register_blueprint(api_client_bp)

with app.app_context():
        os.makedirs(app.instance_path, exist_ok=True)
        db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# Este bloco só serve localmente, ignora no Gunicorn
if __name__ == "__main__":
    app.run(debug=True)
