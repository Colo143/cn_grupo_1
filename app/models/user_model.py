from ..database import DatabaseConnection

class User:
    def __init__(self, user_id = None, nombre = None, apellido = None,
                 contrasenia = None, fecha_nac = None, user_name = None, email = None):
        self.user_id = user_id
        self.nombre = nombre
        self.apellido = apellido
        self.contrasenia = contrasenia
        self.fecha_nac = fecha_nac
        self.user_name = user_name
        self.email = email
    
    @classmethod
    def get(cls, user):
        query = """SELECT user_id, nombre, apellido, contrasenia,
        fecha_nac, user_name, email FROM discord.user WHERE user_id = %s"""
        params = user.user_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return cls(*result)
        return None
    
    @classmethod
    def get_all(cls):
        query = """SELECT user_id, nombre, apellido, contrasenia,
        fecha_nac, user_name, email FROM discord.user"""
        results = DatabaseConnection.fetch_all(query)
        users = []
        if results is not None:
            for result in results:
                users.append(cls(*result))
        return users
    
    @classmethod
    def create(cls, user):
        query = """INSERT INTO discord.user (nombre, apellido, contrasenia, fecha_nac,
        user_name, email) VALUES (%s,%s,%s,%s,%s,%s)"""
        params = (
            user.nombre,
            user.apellido,
            user.contrasenia,
            user.fecha_nac,
            user.user_name,
            user.email
        )
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, user):
        allowed_columns = {'nombre', 'apellido', 'contrasenia', 'fecha_nac',
                           'user_name', 'email'}
        query_parts = []
        params = []
        for key, value in user.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(user.user_id)

        query = "UPDATE discord.user SET " + ", ".join(query_parts) + " WHERE user_id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, user):
        query = "DELETE FROM discord.user WHERE user_id = %s"
        params = user.user_id,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def exists(cls,user_id):
        print(user_id)
        query = '''select * FROM discord.user WHERE user_id = %s'''
        params = user_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        else:
            return False
        
    @classmethod
    def login(cls,user):
        query = '''select user_name, contrasenia from discord.user where user_name=%s and contrasenia=%s'''
        params = user.user_name, user.contrasenia
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            user_data = {
            'user_name': result[0],  # El índice 0 contiene el nombre de usuario
            'contrasenia': result[1]  # El índice 1 contiene la contraseña
            }
            authenticated_user = User(**user_data)
            return authenticated_user
        else:
            return None

    
    
