import re
import spacy
import emoji
import string

nlp = spacy.load("en_core_web_sm")

SELF_HARM_PATTERNS = [
    r'i (hate|dislike) myself',
    r'(want|wish) to die'
]

english_stopwords = set([
    'a', 'an', 'ain', 'any', 'as', 'at', 'the', 'be' 'but', 'by', 'and', 'for', 'from', 'if', 'in', 'into',
    'have', 'ma', 'of', 'off', 'on', 'once', 'only', 'or', 're', 'same', 'so', 'some', 'such', 'than', 'that', 'to', 'too',
    'under', 'up', 've', 'with', 'y', 'those', 'these', 'this', 'there', 'through' 
])


def clean_text(text):
    """
    Полная очистка текста с сохранением эмоционально значимых элементов
    """

    if not isinstance(text, str):
        return ""
    
    # Удаление URL и HTML-тегов
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'<.*?>', '', text)
    
    # Обработка эмодзи (сохраняем их текстовое описание)
    text = emoji.demojize(text, delimiters=(" ", " "))
    
    # Удаление имен пользователей (@username)
    text = re.sub(r'@\w+', '', text)
    
    # Удаление специальных символов (кроме пунктуации)
    text = re.sub(r'[^\w\s.,!?;:\']', '', text)

    # Удаление цифр
    text = re.sub(r'\d+', '', text)
    
    # Приведение к нижнему регистру
    text = text.lower()
    
    # Удаление пунктуации (кроме эмоционально значимой: ! ? ...)
    translator = str.maketrans('', '', string.punctuation.replace('!', '').replace('?', ''))
    text = text.translate(translator)

    # Удаление лишних пробелов
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def flag_self_harm(text):
    for pattern in SELF_HARM_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            text = f"[SELF_HARM_FLAG] {text}"
    return text


def lemmatization(text):
    # Лемматизация (сохраняя контекст)
    doc = nlp(text)
    words = [token.lemma_ for token in doc if token.lemma_.lower() not in english_stopwords]
    text = ' '.join(words)

    # Сохранение многоточий как отдельного токена (индикатор депрессивных текстов)
    text = re.sub(r'\.{3,}', ' ... ', text)

    return text