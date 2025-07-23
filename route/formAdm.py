from flask import request, Blueprint

admin_bp= Blueprint('admin', __name__)

@admin_bp.route('/form', methods=['POST'])
def form_adm():
    data = request.form
    
    return "Form submitted successfully with data: {}".format(data)