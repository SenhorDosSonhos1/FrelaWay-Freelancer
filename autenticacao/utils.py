import re
from django.contrib.messages import constants
from django.contrib import messages

def register_valid_inputs(request, username, password, confirm_password):
    if len(username) <= 3:
        messages.add_message(request, constants.ERROR, 'O nome de usuário precisa ter no mínimo 3 caracteres.')
        return False
    
    elif len(username) > 20:
         messages.add_message(request, constants.ERROR, 'O nome de usuário precisa ter no máximo 20 caracteres.')
         return False
        
    elif re.search(r'[^a-zA-Z0-9_]', username):
        messages.add_message(request, constants.ERROR, 'O nome de usuário só é aceito com caracteres alfanuméricos e underscores (_).')
        return False
    
    elif re.search(r'[^a-zA-Z0-9_#@$%]', password):
        messages.add_message(request, constants.ERROR, 'A senha não pode conter caracteres inválidos, como espaços.')
        return False

    elif len(password) < 6:
        messages.add_message(request, constants.ERROR, 'A senha do usúario precisa ter no mínimo 6 caracteres.')
        return False 
    
    elif len(password) > 16:
        messages.add_message(request, constants.ERROR, 'A senha do usúario precisa ter no máximo 16 caracteres.')
        return False
    
    elif not (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password)):
        messages.add_message(request, constants.ERROR, 'A senha do usúario precisa ter pelo menos 1 letra maiscula, 1 minuscula e pelo menos 1 numero inteiro.')
        return False
    
    elif password != confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas devem ser iguais.')
        return False
    
    return True