# 🔍 DS_Store Decryptor (CLI)

Alat forensik digital sederhana untuk mendekripsi dan menganalisis file `.DS_Store`, baik dari file lokal maupun URL target. Sangat cocok untuk keperluan audit keamanan, enumerasi file tersembunyi, dan pengujian penetrasi berbasis macOS-artifact.

---

## 🚀 Fitur

- 🔎 Membaca isi file `.DS_Store`
- 🌐 Mendukung file dari **URL langsung**
- 💻 Mendukung **file lokal**
- ✅ Ringan & mudah digunakan melalui **command line**
- 📄 Menampilkan hanya nama file (tanpa metadata teknis)

---
## Install dependency
```bash
pip install ds_store requests
```
---
## ⚙️ Instalasi
### 1. Clone repo
```bash
git clone https://github.com/rizqimaulanaa/DS_StoreDEC/
cd dsstore-decryptor
python3 dsstore_decryptor.py --url https://example.com/.DS_Store
```
## 📌 Catatan
Tool ini dibuat untuk tujuan edukasi dan keamanan. Gunakan secara etis dan hanya pada sistem yang Anda miliki atau memiliki izin untuk diuji.
