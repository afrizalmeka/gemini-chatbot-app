# Gemini Chatbot App

Contoh aplikasi chatbot untuk Sesi 14 (Python Programming for AI - Batch 8) - menggabungkan Gemini API (LLM, dipelajari di Sesi 13) dengan antarmuka Streamlit (dipelajari di Sesi 14). Ini realisasi hands-on dari demo yang ditunjukkan di slide "Demo Live: Streamlit Chatbot dengan Gemini" (Sesi 13).

## Struktur Folder

```
gemini-chatbot-app/
├── app.py               # Streamlit - chatbot dengan Gemini API
├── requirements.txt     # Daftar dependency Python
├── .gitignore
└── README.md
```

## Cara Kerja

- **`app.py`** - satu file berisi seluruh logika chatbot: membuat client Gemini, membuat sesi chat (`client.chats.create()`), menampilkan riwayat percakapan, dan mengirim/menerima pesan lewat `st.chat_input()` dan `st.chat_message()`.
- Riwayat percakapan (dan koneksi ke Gemini) disimpan di `st.session_state`, supaya tidak hilang setiap kali Streamlit menjalankan ulang skripnya (Streamlit menjalankan ulang seluruh file dari atas setiap ada interaksi baru dari pengguna).

## Instalasi

Pastikan Python 3.9+ sudah terpasang. Dari dalam folder ini, jalankan:

```bash
pip install -r requirements.txt
```

## Menyiapkan API Key

Buka `app.py`, ganti baris:

```python
api_key = "GANTI_DENGAN_API_KEY_ANDA"
```

dengan API key Gemini kamu sendiri. Lihat `Panduan_Gemini_API_Key_dan_Test.docx` di folder `Sesi13_AI_Generatif_dan_LLM_API/` kalau belum punya API key.

## Menjalankan Aplikasi

```bash
streamlit run app.py
```

Browser akan terbuka otomatis menampilkan antarmuka chat. Ketik pesan di kolom bawah, tekan Enter, dan chatbot akan membalas menggunakan Gemini API.

## Troubleshooting

Masalah umum (module not found, port bentrok, dsb) sama dengan yang dijelaskan di `Panduan_Setup_dan_Troubleshooting_Sesi14.docx` di folder induk. Beberapa yang khusus untuk aplikasi ini:

- **`RuntimeError: Cannot send a request, as the client has been closed`** - pastikan `client` Gemini dibuat dan disimpan di `st.session_state`, bukan sebagai variabel biasa di luar - kalau dibuat ulang setiap rerun, sesi chat lama jadi tidak valid lagi.
- **Error terkait API key** - lihat bagian Troubleshooting di `Panduan_Gemini_API_Key_dan_Test.docx` (Sesi 13), mencakup error model tidak ditemukan, kuota habis, dan API key tidak valid.

## Konteks

Bagian dari materi Sesi 14 - Model Serving & AI Deployment, kurikulum Python Programming for AI Batch 8 (rubythalib.ai). Menggabungkan konsep Sesi 13 (LLM API) dengan Sesi 14 (Streamlit deployment).
