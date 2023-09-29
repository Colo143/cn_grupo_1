from flask import Blueprint, render_template

from ..controllers.server_controller import ServerController

server_bp = Blueprint('server_bp', __name__)

@server_bp.route('/server_register', methods=['GET'])
def show_registration_form():
    return render_template("input_pages/server_registration_form.html")

@server_bp.route('/server_update', methods=['GET'])
def show_modify_form():
    return render_template("input_pages/server_update_form.html")

server_bp.route('/all_servers', methods=['GET'])(ServerController.get_all)
server_bp.route('/get/server/<int:user_id>', methods=['GET'])(ServerController.get)
server_bp.route('/registered_server', methods=['POST'])(ServerController.create)
server_bp.route('/updated_server', methods=['POST'])(ServerController.update)
server_bp.route('/delete/server/<int:user_id>', methods=['DELETE'])(ServerController.delete)