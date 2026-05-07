# Database Schema

## Deskripsi Aplikasi
Aplikasi manajemen tugas mahasiswa yang memungkinkan pengguna
membuat, mengelola, dan memantau progres tugas perkuliahan.

---

## Tabel-Tabel Utama

### 1. Tabel `users`
Menyimpan data akun pengguna aplikasi.

| Kolom | Tipe Data | Keterangan |
|---|---|---|
| id | INT (PK, Auto Increment) | ID unik pengguna |
| username | VARCHAR(50) | Nama pengguna, unik |
| email | VARCHAR(100) | Email, unik |
| password | VARCHAR(255) | Password terenkripsi (hash) |
| avatar_url | VARCHAR(255) | URL foto profil |
| created_at | TIMESTAMP | Waktu akun dibuat |

---

### 2. Tabel `tasks`
Menyimpan data tugas yang dibuat oleh pengguna.

| Kolom | Tipe Data | Keterangan |
|---|---|---|
| id | INT (PK, Auto Increment) | ID unik tugas |
| user_id | INT (FK → users.id) | Pemilik tugas |
| title | VARCHAR(200) | Judul tugas |
| description | TEXT | Deskripsi tugas |
| due_date | DATE | Batas waktu pengumpulan |
| status | ENUM('todo','in_progress','done') | Status tugas |
| created_at | TIMESTAMP | Waktu tugas dibuat |

---

### 3. Tabel `categories`
Menyimpan kategori/mata kuliah untuk pengelompokan tugas.

| Kolom | Tipe Data | Keterangan |
|---|---|---|
| id | INT (PK, Auto Increment) | ID unik kategori |
| user_id | INT (FK → users.id) | Pemilik kategori |
| name | VARCHAR(100) | Nama kategori (mis: "Pemrograman Web") |
| color | VARCHAR(7) | Kode warna hex (mis: "#FF5733") |

---

## Relasi Antar Tabel
- Satu `user` dapat memiliki banyak `tasks` (One-to-Many)
- Satu `user` dapat memiliki banyak `categories` (One-to-Many)
- Satu `task` dapat memiliki satu `category` (Many-to-One)