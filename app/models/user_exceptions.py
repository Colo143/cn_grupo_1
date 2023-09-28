
class CustomException(Exception):
    def __init__(self, status_code, name, description): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

class FilmNotFound(CustomException):
    def __init__(self, user_id):
        if user_id is not None:
            description = f"Film with id {user_id} not found"
        else:
            description = f"User not found in database."    
        super().__init__(404, "Film Not Found", description)

class InvalidDataError(CustomException):
    def __init__(self, description):
        super().__init__(400, "Invalid Data Error", description)
