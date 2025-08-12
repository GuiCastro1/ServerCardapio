from flask import Blueprint, jsonify
from models.cardapio import Plates
from collections import defaultdict

api_client_bp = Blueprint('api_client_bp', __name__)

@api_client_bp.route('/api/products', methods=['GET'])
def get_products():
    products = Plates.query.all()
    grouped = defaultdict(list)

    for p in products:
        grouped[p.type].append({
            'id': p.id,
            'name': p.name,
            'price': float(p.price),
            'type': p.type,
            'url_image': p.url_image,
            'company': p.get_company()
        })

    return jsonify(grouped)