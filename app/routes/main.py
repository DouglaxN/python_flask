from flask import Blueprint, jsonify, request, current_app
from app.models.user import LoginPayload
from pydantic import ValidationError
from app import db
from bson import ObjectId
from app.models.products import *



main_bp = Blueprint('main_bp', __name__)

# O sistema deve permitir que um usuário se autentique para obter um token de acesso
@main_bp.route('/login', methods=['POST'])
def login():
    try:
        # Verifica se o corpo da requisição é JSON
        raw_data = request.get_json()
        # ** Desacopla o dicionário raw_data para criar uma instância de LoginPayload
        user_data = LoginPayload(**raw_data)
    except ValidationError as e:
        return jsonify({"error": "Dados de login inválidos", "details": e.errors()}), 400
    
    except Exception as e:
        return jsonify({"error": "Ocorreu um erro durante o login", "details": str(e)}), 500
    
    if user_data.username == 'admin' and user_data.password == '123':
        return jsonify({"message:" "Login bem-sucedidio!"})
    else: 
        return jsonify({"error": "Credenciais inválidas"})
        

# O sistema deve permitir listagem de todos os produtos disponíveis
@main_bp.route('/products', methods=['GET'])
def get_products():
    products_cursor = db.products.find({})
    products_list = [ProductDBModel(**product).model_dump(by_alias=True, exclude_defaults=True) for product in products_cursor]
    return jsonify({products_list})


# O sistema deve permitir a criação de um novo prouto
@main_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({"message": "Esta é a rota de criação de produtos"})


# O sistema deve permitir a visualição dos detalhes de um unico produto
@main_bp.route('/products/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        oid = ObjectId(product_id)
    except Exception as e:
        return jsonify({"error": f"Erro ao transformar o {product_id} em ObjectID: {e}"})

    product = db.products.find_one({"_id": oid})

    if product:
        product_model = ProductDBModel(**product).model_dump(by_alias=True, exclude_none=True)
        return jsonify(product_model)
    else:
        return jsonify({"error": f"Produto com o id: {product_id} - Não encontrado"})


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
