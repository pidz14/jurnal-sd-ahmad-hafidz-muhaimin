import os
from dotenv import load_dotenv

# Membaca file .env
load_dotenv()

# Mengambil password database
db_password = os.getenv("DB_PASSWORD")

print("Database Password:", db_password)