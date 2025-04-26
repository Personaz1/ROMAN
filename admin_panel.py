import streamlit as st
import google.genai as genai
import os

# --- UI ---
st.set_page_config(page_title="Gemini 2.5 Admin Chat", layout="centered")
st.title("💬 Gemini 2.5 Admin Chat Panel")

# --- Настройки ---
def get_settings():
    if 'system_prompt' not in st.session_state:
        st.session_state['system_prompt'] = "You are Gemini 2.5."
    if 'api_key' not in st.session_state:
        st.session_state['api_key'] = ''
    return st.session_state['system_prompt'], st.session_state['api_key']

with st.sidebar:
    st.header("⚙️ Настройки")
    api_key = st.text_input("API Key", value=st.session_state.get('api_key', ''), type="password")
    system_prompt = st.text_area("Системный промпт", value=st.session_state.get('system_prompt', ''), height=100)
    if st.button("Сохранить настройки"):
        st.session_state['api_key'] = api_key
        st.session_state['system_prompt'] = system_prompt
        st.success("Настройки сохранены!")

system_prompt, api_key = get_settings()

# --- Проверка API ключа ---
if not api_key:
    st.warning("Пожалуйста, введите API ключ Gemini в настройках слева.")
    st.stop()

# --- Инициализация Gemini ---
client = genai.Client(api_key=api_key)

# --- Выводим список доступных моделей в консоль для отладки ---
try:
    print("\nДоступные модели Gemini:")
    for m in client.models.list():
        print(m)
except Exception as e:
    print(f"[Ошибка получения списка моделей]: {e}")

# --- История чата ---
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# --- UI чата ---
st.subheader("Чат с Gemini 2.5")
for msg in st.session_state['chat_history']:
    role, text = msg
    align = 'user' if role == 'user' else 'assistant'
    st.chat_message(align).write(text)

user_input = st.chat_input("Введите сообщение...")
if user_input:
    st.session_state['chat_history'].append(('user', user_input))
    with st.spinner("Gemini думает..."):
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash',
                contents=user_input,
                config=genai.types.GenerateContentConfig(
                    system_instruction=system_prompt
                )
            )
            answer = response.text
        except Exception as e:
            answer = f"Ошибка: {e}"
        st.session_state['chat_history'].append(('assistant', answer))
        st.rerun() 