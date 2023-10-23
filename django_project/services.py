from transliterate import translit


def translate_text(text: str):
    text = str(translit(text, 'ru',  reversed=True)).replace(' ', '_').lower()
    return text




