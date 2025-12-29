# Task Management App

Aplikasi Task Management berbasis web yang dikembangkan untuk memenuhi **Take Home Test AI Engineer**. Aplikasi ini dibangun menggunakan arsitektur Clean Code sederhana dengan fitur autentikasi JWT dan manajemen tugas (CRUD).

## 🛠 Tech Stack

**Frontend:**
* Vue.js 3 (Composition API)
* Tailwind CSS (Modern styling)
* Axios (HTTP Client)
* Vite (Build tool)

**Backend:**
* Python 3
* Flask (REST API)
* Flask-SQLAlchemy (ORM)
* Flask-JWT-Extended (Authentication)
* PostgreSQL (Database)

## 📋 Prasyarat (Prerequisites)

Sebelum menjalankan aplikasi, pastikan komputer Anda memiliki:
1.  **Python 3.x**
2.  **Node.js** & **npm**
3.  **PostgreSQL**

## 🚀 Panduan Instalasi & Menjalankan Aplikasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di lingkungan lokal (local environment).

### 1. Setup Database
Pastikan PostgreSQL service sudah berjalan, lalu buat database baru bernama `task_db`:

```sql
CREATE DATABASE task_db;
```

### 2. Setup Backend (Flask)

Buka terminal dan masuk ke direktori backend:

```bash
cd backend
```

(Opsional) Buat dan aktifkan virtual environment:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

Install dependensi yang dibutuhkan:
```bash
pip install -r requirements.txt
```

**Konfigurasi Database:**
Buka file `config.py` dan sesuaikan `SQLALCHEMY_DATABASE_URI` dengan kredensial PostgreSQL Anda (username & password).

```python
# Format: postgresql://username:password@localhost/nama_database
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@localhost/task_db'
```

Jalankan server Flask:
```bash
python app.py
```
*Server Backend akan berjalan di: `http://127.0.0.1:5000`*

### 3. Setup Frontend (Vue.js)

Buka terminal baru, lalu masuk ke direktori frontend:

```bash
cd frontend
```

Install module yang diperlukan:
```bash
npm install
```

Jalankan server development:
```bash
npm run dev
```
*Frontend biasanya akan berjalan di: `http://localhost:5173`*

---

## 🔐 Akun Login (Testing)

Sesuai spesifikasi tugas, sistem login menggunakan kredensial statis (hardcoded dummy login):

* **Username:** `admin`
* **Password:** `admin123`

---

## 📂 Struktur Folder Project

Berikut adalah gambaran struktur folder utama aplikasi ini:

```
task-management-app/
├── backend/                  # Server-side Logic
│   ├── app.py                # Entry point & App Initialization
│   ├── config.py             # Database & JWT Config
│   ├── models.py             # Database Models (SQLAlchemy)
│   ├── routes.py             # API Routes / Endpoints
│   └── requirements.txt      # Python dependencies list
│
├── frontend/                 # Client-side Interface
│   ├── src/
│   │   ├── assets/           # CSS & Static files
│   │   ├── components/       # Vue Components
│   │   │   ├── Login.vue     # Halaman Login
│   │   │   └── TaskManager.vue # Dashboard CRUD Task
│   │   ├── App.vue           # Root Component
│   │   └── main.js           # Vue Entry point
│   ├── index.html
│   ├── tailwind.config.js    # Konfigurasi Tailwind CSS
│   └── package.json
│
└── README.md                 # Dokumentasi Project
```

## 📝 Fitur Utama

1.  **JWT Authentication:** Login aman menggunakan Token Bearer.
2.  **Task CRUD:**
    * **Create:** Menambah tugas baru dengan judul, deskripsi, dan status.
    * **Read:** Menampilkan daftar tugas dalam layout Grid yang responsif.
    * **Update:** Mengedit detail tugas dan mengubah status (To Do -> In Progress -> Done).
    * **Delete:** Menghapus tugas dengan konfirmasi.
3.  **Modern UI/UX:**
    * Desain responsif menggunakan **Tailwind CSS**.
    * Indikator warna status visual (Badges).
    * Interaksi halus (Hover effects, Transitions).

---

**Dibuat oleh:** [Nama Anda]