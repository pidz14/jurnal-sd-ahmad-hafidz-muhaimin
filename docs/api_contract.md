# API Contract - Aplikasi Mahasiswa

## 1. Get User Profile

**Endpoint:** `/api/v1/profile`  
**Method:** `GET`  
**Auth:** Bearer Token  

**Response Body (200 OK):**
```json
{
  "id": 1,
  "username": "mahasiswa_sd",
  "email": "mhs@univ.ac.id",
  "avatar_url": "https://image.com/avatar.png"
}
```

---

## 2. Login

**Endpoint:** `/api/v1/auth/login`  
**Method:** `POST`  
**Auth:** Tidak diperlukan  

**Request Body:**
```json
{
  "email": "mhs@univ.ac.id",
  "password": "password123"
}
```

**Response Body (200 OK):**
```json
{
  "status": "success",
  "message": "Login berhasil",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": 1,
      "username": "mahasiswa_sd",
      "email": "mhs@univ.ac.id"
    }
  }
}
```

**Response Body (401 Unauthorized):**
```json
{
  "status": "error",
  "message": "Email atau password salah"
}
```