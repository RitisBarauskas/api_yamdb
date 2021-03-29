from random import choices
from string import ascii_uppercase, digits


def generate_confirmation_code(length):
    return ''.join(choices(digits + ascii_uppercase, k=length))
