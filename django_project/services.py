import secrets
import string

from transliterate import translit


def translate_text(text: str):
    text = str(translit(text, 'ru',  reversed=True)).replace(' ', '_').lower()
    return text


def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


def generate_name(length):
    alphabet = string.ascii_letters
    name = ''.join(secrets.choice(alphabet) for _ in range(length))
    return name

