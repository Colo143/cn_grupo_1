from ..database import DatabaseConnection

class Server:
    def __init__(self, server_id = None, nombre = None, user_id = None):
        self.server_id = server_id
        self.nombre = nombre
        self.user_id = user_id
    
    @classmethod
    def get(cls, server):
        query = """SELECT server_id, nombre, user_id FROM discord.server WHERE server_id = %s"""
        params = server.server_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return cls(*result)
        return None
    
    @classmethod
    def get_all(cls):
        query = """SELECT server_id, nombre, user_id FROM discord.server"""
        results = DatabaseConnection.fetch_all(query)
        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(*result))
        return servers
    
    @classmethod
    def create(cls, server):
        query = """INSERT INTO discord.server (server_id, nombre, user_id) VALUES 
        (%s,%s,%s)"""
        params = (
            server.nombre,
            server.apellido,
            server.contrasenia,
            server.fecha_nac,
            server.user_name,
            server.email
        )
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, server):
        allowed_columns = {'server_id', 'nombre', 'user_id'}
        query_parts = []
        params = []
        for key, value in server.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(server.server_id)

        query = "UPDATE discord.server SET " + ", ".join(query_parts) + " WHERE user_id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, server):
        query = "DELETE FROM discord.server WHERE server_id = %s"
        params = server.user_id,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def exists(cls,server_id):
        query = '''select * FROM discord.server WHERE server_id = %s'''
        params = server_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        else:
            return False