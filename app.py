"""
app.py - Chatbot Gemini dengan antarmuka Streamlit.
Menggabungkan LLM API (Sesi 13) dengan UI Streamlit (Sesi 14) - persis
seperti demo yang ditunjukkan di slide 60 Sesi 13.
Jalankan dari terminal (folder ini) dengan:
    streamlit run app.py
"""
import streamlit as st
from google import genai

# Ganti dengan API key Gemini kamu sendiri (lihat Panduan_Gemini_API_Key_dan_Test.docx
# di folder Sesi13 kalau belum punya).
api_key = "GANTI_DENGAN_API_KEY_ANDA"

st.title("Chatbot Gemini")
st.write("Contoh aplikasi chatbot sederhana - menggabungkan LLM API (Sesi 13) dengan Streamlit (Sesi 14).")

# st.session_state menyimpan data yang tetap ada antar interaksi pengguna -
# tanpa ini, riwayat chat akan hilang tiap kali Streamlit menjalankan ulang skrip
# (Streamlit menjalankan ulang SELURUH skrip dari atas setiap ada interaksi baru).
#
# PENTING: client JUGA harus disimpan di session_state, bukan dibuat sebagai variabel
# biasa di luar - kalau tidak, setiap kali skrip dijalankan ulang akan tercipta client
# BARU, sementara objek chat di session_state masih terikat ke client LAMA yang sudah
# tidak aktif, menyebabkan error "Cannot send a request, as the client has been closed".
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=api_key)

if "chat" not in st.session_state:
    # client.chats.create() membuat sesi percakapan yang otomatis mengingat
    # riwayat pesan sebelumnya - sama seperti dipelajari di notebook Sesi 13.
    st.session_state.chat = st.session_state.client.chats.create(model="gemini-3.5-flash")
    st.session_state.history = []

# Tampilkan ulang seluruh riwayat percakapan setiap kali skrip dijalankan ulang,
# supaya pesan-pesan lama tidak hilang dari layar.
for role, text in st.session_state.history:
    with st.chat_message(role):
        st.write(text)

# st.chat_input() adalah kolom input khusus gaya chat, muncul menempel di bawah layar.
# Nilainya berupa teks yang diketik pengguna, atau None kalau belum ada yang dikirim.
prompt = st.chat_input("Ketik pesan...")

if prompt:
    # Simpan dan tampilkan pesan pengguna terlebih dulu.
    st.session_state.history.append(("user", prompt))
    with st.chat_message("user"):
        st.write(prompt)

    # Kirim pesan ke Gemini lewat sesi chat yang sudah dibuat - otomatis
    # membawa konteks percakapan sebelumnya.
    response = st.session_state.chat.send_message(prompt)
    reply = response.text

    # Simpan dan tampilkan balasan chatbot.
    st.session_state.history.append(("assistant", reply))
    with st.chat_message("assistant"):
        st.write(reply)
