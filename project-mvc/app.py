import os
import time

# Membaca variabel lingkungan dengan nilai default
user_name = os.getenv('APP_USER', 'Guest')
app_env = os.getenv('APP_ENV', 'development')

if __name__ == "__main__":
    print(f"Halo {user_name}! Aplikasi ini berjalan di dalam kontainer Docker.")
    print(f"Status Lingkungan: {app_env}")
    
    # --- TRIK AGAR KONTAINER TIDAK LANGSUNG MATI ---
    print("Kontainer standby... Tekan Ctrl+C di terminal nanti untuk stop.")
    while True:
        time.sleep(1)  # Menahan program agar terus berjalan setiap 1 detik