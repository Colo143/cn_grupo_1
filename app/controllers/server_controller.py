from ..models.server_model import Server
from app.models.exceptions import DataNotFound, InvalidDataError

from flask import render_template
from flask import request

class ServerController:

    @classmethod
    def get(cls, server_id):
        server = Server(server_id=server_id)
        result = Server.get(server)
        if result is not None:
            return render_template("result_pages/server_details_id.html", server=result), 200
        else:
            raise DataNotFound(server_id)
        
    @classmethod
    def get_all(cls):
        server_objects = Server.get_all()
        servers = []
        for server in server_objects:
            servers.append(server)
        
        return render_template("result_pages/server_list.html", servers=servers), 200
    
    @classmethod
    def create(cls):
        try:
            nombre = request.form.get('nombre')
            user_id = request.form.get('user_id')

            if nombre is not None:
                if not nombre.replace(" ", "").isalpha() and not nombre.isspace():
                    raise InvalidDataError("El valor del campo 'nombre' no es valido.")

            # Más validaciones según tus requisitos

            # Si todas las validaciones son exitosas, crea el objeto User
            data = {
                'nombre': nombre,
                'user_id': user_id
            }

            server = Server(**data)
            Server.create(server)

            return render_template("result_pages/server_welcome.html", server=server), 201

        except InvalidDataError as e:
            raise e


    @classmethod
    def update(cls):
        try:
            server_id = request.form.get('server_id')
            if Server.exists(server_id):

                nombre = request.form.get('nombre')
                user_id = request.form.get('user_id')
                
                if nombre is not None:
                    if not nombre.replace(" ", "").isalpha() and not nombre.isspace():
                        raise InvalidDataError("El valor del campo 'nombre' no es valido.")

                # Si todas las validaciones son exitosas, crea el objeto User
                data = {
                    'nombre': nombre,
                    'user_id': user_id,
                    'server_id': server_id
                }

                server = Server(**data)
                Server.update(server)
                return render_template("result_pages/server_modified.html", server=server), 200
            else:
                raise DataNotFound(server_id)
        except InvalidDataError as e:
            raise e
        
    @classmethod
    def delete(cls, server_id):
        """Delete a film"""
        if Server.exists(server_id):
            server = Server(server_id=server_id)
            # TODO: Validate film exists
            Server.delete(server)
            return render_template("result_pages/server_deleted.html", server=server), 204
        else:
            raise DataNotFound(server_id).get_response()