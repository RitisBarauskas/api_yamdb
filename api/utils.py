from random import choices
from string import digits, ascii_uppercase


def generate_confirmation_code(length):
    return ''.join(choices(digits + ascii_uppercase, k=length))
