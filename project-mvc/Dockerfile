# 1. Menggunakan base image Python resmi yang ringan
FROM python:3.9-slim

# 2. Menentukan folder kerja di dalam kontainer nanti
WORKDIR /app

# 3. Menentukan nilai default variabel lingkungan (Soal D.2)
ENV APP_USER="Developer Mahasiswa"
ENV APP_ENV="development"

# 4. Menyalin seluruh isi folder lokal ke dalam folder kerja kontainer [cite: 36]
COPY . .

# 5. Perintah utama untuk menjalankan aplikasi Python saat kontainer menyala [cite: 37]
CMD ["python", "app.py"]