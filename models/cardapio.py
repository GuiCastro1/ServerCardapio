from flask_sqlalchemy import SQLAlchemy
import json
db = SQLAlchemy()

class Plates(db.Model):
    __tablename__  = 'cardapio'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    url_image = db.Column(db.String(100), nullable=False)
    type  = db.Column(db.String(25), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)

    def set_company(self, lst):
        """Converte lista Python para JSON e salva no banco."""
        self.company = json.dumps(lst, ensure_ascii=False)

    def get_company(self):
        """Converte string JSON do banco para lista Python."""
        return json.loads(self.company) if self.company else []