from flask import request, Blueprint, jsonify
from models.cardapio import db, Plates
from modules.utilsImg.processImage import process_image

create_bp = Blueprint('teste',__name__)

@create_bp.route('/form', methods=['POST'])
def form_adm():
    try:
        company = request.form.getlist('company')
        image = request.files['image']
        tp = request.form['category']
        image_path = process_image(image, tp)

        # Converter preço, substituindo vírgula por ponto
        price_str = request.form['price']
        price_float = float(price_str.replace(',', '.'))

        item = Plates(
                name=request.form['name'],
                # price=request.form['price'],
                price=price_float,
                type=tp,
                url_image=image_path,
        )
        item.set_company(company)

        db.session.add(item)
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'Produto criado com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'Erro ao criar produto: {str(e)}'})

        

