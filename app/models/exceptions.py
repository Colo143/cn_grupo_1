
class CustomException(Exception):
    def __init__(self, status_code, name, description): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

class DataNotFound(CustomException):
    def __init__(self, user_id):
        if user_id is not None:
            description = f"Dato con id {user_id} no encontrado."
        else:
            description = f"Dato inexsistene en base de datos."    
        super().__init__(404, "Dato no encontrado.", description)

class InvalidDataError(CustomException):
    def __init__(self, description):
        super().__init__(400, "Error de datos no válidos", description)
