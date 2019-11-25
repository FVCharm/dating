from flask import request, jsonify

from app.api import bp
from app.forms.user import RegisterForm
from app.models.user import User
from app.errors.error_code import Success
from app.api.auth import token_auth


@bp.route('/register', methods=['POST'])
def create_user():
    '''注册一个新用户'''
    data = request.json
    form = RegisterForm(data=data)
    form.validate_for_api()
    User.register_by_phone(form.name.data,
                           form.phone.data,
                           form.password.data)
    return Success()


@bp.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    '''返回一个用户'''
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users', methods=['GET'])
def get_users():
    '''返回用户集合，分页'''
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """ 修改一个用户 """
    pass


@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    '''删除一个用户'''
    pass
