from flask import Blueprint, render_template

from ..controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['GET'])
def show_registration_form():
    return render_template("input_pages/user_registration_form.html")

@user_bp.route('/update', methods=['GET'])
def show_modify_form():
    return render_template("input_pages/user_update_form.html")

@user_bp.route('/login', methods = ['GET'])
def show_login_user():
    return render_template("input_pages/user_log_in.html")

user_bp.route('/logged', methods=['POST'])(UserController.login)
user_bp.route('/all_users', methods=['GET'])(UserController.get_all)
user_bp.route('/get/user/<int:user_id>', methods=['GET'])(UserController.get)
user_bp.route('/registered_user', methods=['POST'])(UserController.create)
user_bp.route('/updated_user', methods=['POST'])(UserController.update)
user_bp.route('/delete/user/<int:user_id>', methods=['GET'])(UserController.delete)