from flask import Blueprint, jsonify

main_bp = Blueprint('main_bp', __name__)

# O sistema deve permitir que um usuário se autentique para obter um token de acesso
@main_bp.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Realizar o login"})

# O sistema deve permitir listagem de todos os produtos disponíveis
@main_bp.route('/products', methods=['GET'])
def get_products():
    return jsonify({"message": "Esta é a rota de listagem dos produtos"})

# O sistema deve permitir a criação de um novo prouto
@main_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({"message": "Esta é a rota de criação de produtos"})

# O sistema deve permitir a visualição dos detalhes de um unico produto
@main_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return jsonify({"message": f"Esta é a rota de visualização do id do produto {product_id}"})

# O sistema deve permitir a atualização de um único produto e produto existente
@main_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return jsonify({"message": f"Esta é a rota de atualização do id do produto {product_id}"})

# O sistema deve permitir a deleção de um unico produto e produto existente
@main_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return jsonify({"message": f"Esta é a rota de deleção do id do produto {product_id}"})

# O sistema deve permitir a importação de vendas através de um arquivo
@main_bp.route('/sales/upload', methods=['POST'])
def upload_sales():
    return jsonify({"message": "Esta é a rota de importação de vendas"})


@main_bp.route('/')
def index():
    return jsonify({"message": "Bem vindo ao Flask API!"})
