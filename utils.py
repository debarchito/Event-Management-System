from string import ascii_uppercase, ascii_lowercase, digits
from random import choice

def generate_unique_id():
    chars = ascii_uppercase + ascii_lowercase + digits
    return ''.join(choice(chars) for _ in range(10))
