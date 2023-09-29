from ..models.channel_model import Channel
from app.models.exceptions import DataNotFound, InvalidDataError

from flask import render_template
from flask import request

class ChannelController:

    @classmethod
    def get(cls, channel_id):
        channel = Channel(channel_id=channel_id)
        result = Channel.get(channel)
        if result is not None:
            return render_template("result_pages/channel_details_id.html", channel=result), 200
        else:
            raise DataNotFound(channel_id)
        
    @classmethod
    def get_all(cls):
        channel_objects = Channel.get_all()
        channels = []
        for channel in channel_objects:
            channels.append(channel)
        
        return render_template("result_pages/channel_list.html", channels=channels), 200
    
    @classmethod
    def create(cls):
        try:
            nombre = request.form.get('nombre')
            server_id = request.form.get('server_id')

            if nombre is not None:
                if not nombre.replace(" ", "").isalpha() and not nombre.isspace():
                    raise InvalidDataError("El valor del campo 'nombre' no es valido.")

            # Si todas las validaciones son exitosas, crea el objeto User
            data = {
                'nombre': nombre,
                'server_id': server_id
            }

            channel = Channel(**data)
            Channel.create(channel)

            return render_template("result_pages/channel_welcome.html", channel=channel), 201

        except InvalidDataError as e:
            raise e


    @classmethod
    def update(cls):
        try:
            channel_id = request.form.get('channel_id')
            if Channel.exists(channel_id):

                nombre = request.form.get('nombre')
                server_id = request.form.get('server_id')
                
                if nombre is not None:
                    if not nombre.replace(" ", "").isalpha() and not nombre.isspace():
                        raise InvalidDataError("El valor del campo 'nombre' no es valido.")

                # Si todas las validaciones son exitosas, crea el objeto User
                data = {
                    'nombre': nombre,
                    'server_id': server_id,
                    'channel_id': channel_id
                }

                channel = Channel(**data)
                Channel.update(channel)
                return render_template("result_pages/channel_modified.html", channel=channel), 200
            else:
                raise DataNotFound(channel_id)
        except InvalidDataError as e:
            raise e
        
    @classmethod
    def delete(cls, channel_id):
        """Delete a film"""
        if Channel.exists(channel_id):
            channel = Channel(channel_id=channel_id)
            # TODO: Validate film exists
            Channel.delete(channel)
            return render_template("result_pages/channel_deleted.html", channel=channel), 204
        else:
            raise DataNotFound(channel_id).get_response()