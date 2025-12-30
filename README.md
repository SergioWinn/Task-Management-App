# Task Management App

Aplikasi Task Management berbasis web yang dibangun menggunakan arsitektur Clean Code. Aplikasi ini memiliki fitur autentikasi JWT, manajemen tugas (CRUD) lengkap dengan tanggal, serta antarmuka modern yang responsif dan mendukung Dark Mode.

## 🛠 Tech Stack

**Frontend:**
* Vue.js 3 (Composition API)
* Tailwind CSS (Modern styling & Dark Mode)
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

Sistem login menggunakan kredensial statis (dummy login) untuk keperluan demonstrasi:

* **Username:** `admin`
* **Password:** `admin123`

---

## 📝 Fitur Utama

Aplikasi ini memiliki fitur lengkap sebagai berikut:

### 1. Advanced Task Management
* **CRUD Lengkap:** Create, Read, Update, dan Delete tugas.
* **Manajemen Waktu:** Mendukung input **Start Date** dan **Due Date** (Deadline) untuk setiap tugas.
* **Status Tracking:** Mengubah status tugas (To Do, In Progress, Done) dengan indikator visual.

### 2. Search & Filtering (Real-time)
* **Pencarian Instan:** Mencari tugas berdasarkan judul tanpa reload halaman (Computed Properties).
* **Filter Status:** Menyaring tugas berdasarkan status pekerjaan.

### 3. Modern UI/UX (Tailwind CSS)
* **Dark Mode Support:** Mendukung tema gelap dan terang (Sun/Moon toggle) yang tersimpan di LocalStorage.
* **Responsive Design:** Tampilan grid yang rapi di desktop maupun mobile.
* **Interactive Login:** Fitur Show/Hide password pada form login.

### 4. Security
* **JWT Authentication:** Mengamankan endpoint API menggunakan Token Bearer.

---

## 📂 Struktur Folder Project

```
task-management-app/
├── backend/                  # Server-side Logic
│   ├── app.py                # Entry point & App Initialization
│   ├── config.py             # Database & JWT Config
│   ├── models.py             # Database Models (Task with Dates)
│   ├── routes.py             # API Routes / Endpoints
│   └── requirements.txt      # Python dependencies list
│
├── frontend/                 # Client-side Interface
│   ├── src/
│   │   ├── assets/           # CSS & Static files
│   │   ├── components/       # Vue Components
│   │   │   ├── Login.vue     # Halaman Login (Show/Hide Pass)
│   │   │   └── TaskManager.vue # Dashboard (Search, Filter, Date)
│   │   ├── App.vue           # Root Component (Dark Mode Logic)
│   │   └── main.js           # Vue Entry point
│   ├── index.html
│   ├── tailwind.config.js    # Konfigurasi Tailwind & Dark Mode
│   └── package.json
│
└── README.md                 # Dokumentasi Project
```

---

**Dibuat oleh:** Sergio Winnero