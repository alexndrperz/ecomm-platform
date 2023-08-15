import secrets

import random
import string

def generate_token(num):
    characters = string.ascii_letters + string.digits
    token = ''.join(random.choices(characters, k=num))
    return f'{token}'

def generate_access_token():
        token = secrets.token_urlsafe(32)
        enlace = f"{token}"
        return enlace