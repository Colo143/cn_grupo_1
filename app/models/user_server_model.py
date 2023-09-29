from ..database import DatabaseConnection

class UserServer:
    def __init__(self, userxserver_id = None,user_id = None, server_id = None):
        self.userxserver_id = userxserver_id
        self.user_id = user_id
        self.server_id = server_id
    
    @classmethod
    def create(cls, userxserver):
        query = """INSERT INTO discord.userxserver (user_id, server_id) VALUES (%s,%s)"""
        params = (
            userxserver.user_id,
            userxserver.server_id
        )
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, userxserver):
        allowed_columns = {'user_id', 'server_id'}
        query_parts = []
        params = []
        for key, value in userxserver.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(userxserver.userxserver_id)

        query = "UPDATE discord.userxserver SET " + ", ".join(query_parts) + " WHERE userxserver_id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, userxserver):
        query = "DELETE FROM discord.userxserver WHERE userxserver_id = %s"
        params = userxserver.userxserver_id,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def exists(cls,userxserver_id):
        query = '''select * FROM discord.userxserver WHERE userxserver_id = %s'''
        params = userxserver_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        else:
            return False
        