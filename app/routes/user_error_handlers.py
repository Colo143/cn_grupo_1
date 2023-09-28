from flask import Blueprint, render_template
from ..models.user_exceptions import FilmNotFound, InvalidDataError

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(FilmNotFound)
def handle_not_found(error):
    error_message = error.description
    return render_template("error_pages/error_404.html", error_message=error_message), 404

@errors.app_errorhandler(InvalidDataError)
def handle_bad_request(error):
    error_message = error.description
    return render_template("error_pages/error_400.html", error_message=error_message), 400