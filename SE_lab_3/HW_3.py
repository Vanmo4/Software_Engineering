from transformers import pipeline
import streamlit as st

# Инициализируем модель для перевода с русского на английский
transl = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")

# Заголовок веб-приложения
st.title('Перевод текста')

# Форма для ввода текста
user_input = st.text_area("Введите текст на русском языке", "")

# Кнопка для перевода текста
if st.button('Перевести'):
    # Переводим текст с русского на английский
    transl_text = transl(user_input, max_length=40)[0]['translation_text']
    
    # Выводим результат перевода
    st.markdown(f"Результат перевода: {transl_text}")
