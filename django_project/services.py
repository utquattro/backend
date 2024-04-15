import secrets
import string
from django.conf import settings
from dadata import Dadata
from transliterate import translit


class Address:
    def __init__(self):
        self.value = ""
        self.unrestricted_value = ""
        self.fias_id = ""
        self.city = ""


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


def get_address_list_from_dadata(query):
    token = settings.DADATA_TOKEN
    dadata = Dadata(token)
    result = dadata.suggest("address", query,)
    address_list = []
    for item in result:
        address = Address()
        address.value = item["value"]
        address.unrestricted_value = item["unrestricted_value"]
        address.fias_id = item["data"]["fias_id"]
        address.city = item["data"]["city"]
        address_list.append(address)

    return address_list

