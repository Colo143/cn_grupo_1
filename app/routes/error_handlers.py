from flask import Blueprint, render_template
from ..models.exceptions import DataNotFound, InvalidDataError

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(DataNotFound)
def handle_not_found(error):
    error_message = error.description
    return render_template("error_pages/error_404.html", error_message=error_message), 404

@errors.app_errorhandler(InvalidDataError)
def handle_bad_request(error):
    error_message = error.description
    return render_template("error_pages/error_400.html", error_message=error_message), 400