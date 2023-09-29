from ..database import DatabaseConnection

class Channel:
    def __init__(self, channel_id = None, nombre = None, server_id = None):
        self.channel_id = channel_id
        self.nombre = nombre
        self.server_id = server_id
    
    @classmethod
    def get(cls, channel):
        query = """SELECT channel_id, nombre, server_id FROM discord.channel WHERE channel_id = %s"""
        params = channel.channel_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return cls(*result)
        return None
    
    @classmethod
    def get_all(cls):
        query = """SELECT channel_id, nombre, server_id FROM discord.channel"""
        results = DatabaseConnection.fetch_all(query)
        channels = []
        if results is not None:
            for result in results:
                channels.append(cls(*result))
        return channels
    
    @classmethod
    def create(cls, channel):
        query = """INSERT INTO discord.channel (channel_id, nombre, server_id) VALUES 
        (%s,%s,%s)"""
        params = (
            channel.nombre,
            channel.apellido,
            channel.contrasenia,
            channel.fecha_nac,
            channel.user_name,
            channel.email
        )
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, channel):
        allowed_columns = {'channel_id', 'nombre', 'server_id'}
        query_parts = []
        params = []
        for key, value in channel.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(channel.channel_id)

        query = "UPDATE discord.channel SET " + ", ".join(query_parts) + " WHERE channel_id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, channel):
        query = "DELETE FROM discord.channel WHERE channel_id = %s"
        params = channel.channel_id,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def exists(cls,channel_id):
        query = '''select * FROM discord.channel WHERE channel_id = %s'''
        params = channel_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        else:
            return False