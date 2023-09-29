from ..models.user_model import User
from app.models.exceptions import DataNotFound, InvalidDataError

from flask import render_template
from flask import request

class UserController:

    @classmethod
    def login(cls):
        user_name = request.form.get('user_name')
        contrasenia = request.form.get('contrasenia')
        usuario = User(user_name=user_name, contrasenia=contrasenia)
        user = User.login(usuario)
        if user is not None:
            return render_template("result_pages/login_welcome.html", user=user), 200
        else:
            user_id = None
            raise DataNotFound(user_id)

    @classmethod
    def get(cls, user_id):
        user = User(user_id=user_id)
        result = User.get(user)
        if result is not None:
            return render_template("result_pages/user_details_id.html", user=result), 200
        else:
            raise DataNotFound(user_id)
        
    @classmethod
    def get_all(cls):
        """Get all users"""
        user_objects = User.get_all()
        users = []
        for user in user_objects:
            users.append(user)
        
        # Renderizar la plantilla HTML y pasar la lista de usuarios como contexto
        return render_template("result_pages/user_list.html", users=users), 200
    
    @classmethod
    def create(cls):
        try:
            nombre = request.form.get('nombre')
            apellido = request.form.get('apellido')
            contrasenia = request.form.get('contrasenia')
            fecha_nac = request.form.get('fecha_nac')
            user_name = request.form.get('user_name')
            email = request.form.get('email')

            # Validación para el campo 'nombre': solo letras y espacios
            if nombre is not None:
                if not nombre.replace(" ", "").isalpha() and not nombre.isspace():
                    raise InvalidDataError("El valor del campo 'nombre' no es valido.")

            # Validación para el campo 'apellido': solo letras y espacios
            if apellido is not None:
                if not apellido.replace(" ", "").isalpha() and not apellido.isspace():
                    raise InvalidDataError("El valor del campo 'apellido' no es valido.")

            # Validación para el campo 'contrasenia': alfanumérico
            tiene_letra = False
            tiene_numero = False
            if contrasenia is not None:
                for caracter in contrasenia:
                    if caracter.isalpha():
                        tiene_letra = True
                    elif caracter.isdigit():
                        tiene_numero = True
                    
                    # Si ya encontramos una letra y un número, no es necesario seguir comprobando
                    if tiene_letra and tiene_numero:
                        break
                if not (tiene_letra and tiene_numero):    
                    raise InvalidDataError("El valor del campo 'contrasenia' debe ser alfanumérico.")

            # Validación para el campo 'user_name' (puedes definir tus propias condiciones)
            if user_name is not None:
                if len(user_name) < 3:
                    raise InvalidDataError("El valor del campo 'user_name' debe contener al menos 3 caracteres.")

            # Más validaciones según tus requisitos

            # Si todas las validaciones son exitosas, crea el objeto User
            data = {
                'nombre': nombre,
                'apellido': apellido,
                'contrasenia': contrasenia,
                'fecha_nac': fecha_nac,
                'user_name': user_name,
                'email': email
            }

            user = User(**data)
            User.create(user)

            return render_template("result_pages/user_welcome.html", user=user), 201

        except InvalidDataError as e:
            raise e


    @classmethod
    def update(cls):
        """Update a film"""
        try:
            user_id = request.form.get('user_id')
            if User.exists(user_id):

                nombre = request.form.get('nombre')
                apellido = request.form.get('apellido')
                contrasenia = request.form.get('contrasenia')
                fecha_nac = request.form.get('fecha_nac')
                user_name = request.form.get('user_name')
                email = request.form.get('email')
                
                print(user_name)
                # Validación para el campo 'nombre': solo letras y espacios
                if nombre is not None:
                    if not nombre.replace(" ", "").isalpha() and not nombre.isspace():
                        raise InvalidDataError("El valor del campo 'nombre' no es valido.")

                # Validación para el campo 'apellido': solo letras y espacios
                if apellido is not None:
                    if not apellido.replace(" ", "").isalpha() and not apellido.isspace():
                        raise InvalidDataError("El valor del campo 'apellido' no es valido.")

                # Validación para el campo 'contrasenia': alfanumérico
                tiene_letra = False
                tiene_numero = False
                if contrasenia is not None:
                    for caracter in contrasenia:
                        if caracter.isalpha():
                            tiene_letra = True
                        elif caracter.isdigit():
                            tiene_numero = True
                        
                        # Si ya encontramos una letra y un número, no es necesario seguir comprobando
                        if tiene_letra and tiene_numero:
                            break
                if not (tiene_letra and tiene_numero):    
                        raise InvalidDataError("El valor del campo 'contrasenia' debe ser alfanumérico.")

                # Validación para el campo 'user_name' (puedes definir tus propias condiciones)
                if user_name is not None:
                    if len(user_name) < 3:
                        raise InvalidDataError("El campo 'user_name' debe contener al menos 3 caracteres.")

                # Más validaciones según tus requisitos

                # Si todas las validaciones son exitosas, crea el objeto User
                data = {
                    'nombre': nombre,
                    'apellido': apellido,
                    'contrasenia': contrasenia,
                    'fecha_nac': fecha_nac,
                    'user_name': user_name,
                    'email': email,
                    'user_id': user_id
                }

                user = User(**data)
                User.update(user)
                return render_template("result_pages/user_modified.html", user=user), 200
            else:
                raise DataNotFound(user_id)
        except InvalidDataError as e:
            raise e
        
    @classmethod
    def delete(cls, user_id):
        """Delete a film"""
        if User.exists(user_id):
            user = User(user_id=user_id)
            # TODO: Validate film exists
            User.delete(user)
            return render_template("result_pages/user_deleted.html", user=user), 204
        else:
            raise DataNotFound(user_id)