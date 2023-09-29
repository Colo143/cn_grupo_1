from flask import Blueprint, render_template

from ..controllers.channel_controller import ChannelController

channel_bp = Blueprint('channel_bp', __name__)

@channel_bp.route('/channel_register', methods=['GET'])
def show_registration_form():
    return render_template("input_pages/channel_registration_form.html")

@channel_bp.route('/channel_update', methods=['GET'])
def show_modify_form():
    return render_template("input_pages/channel_update_form.html")

channel_bp.route('/all_channels', methods=['GET'])(ChannelController.get_all)
channel_bp.route('/get/channel/<int:user_id>', methods=['GET'])(ChannelController.get)
channel_bp.route('/registered_channel', methods=['POST'])(ChannelController.create)
channel_bp.route('/updated_channel', methods=['POST'])(ChannelController.update)
channel_bp.route('/delete/channel/<int:user_id>', methods=['DELETE'])(ChannelController.delete)