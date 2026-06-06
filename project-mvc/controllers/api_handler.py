import random

def get_users():
    # Simulasi server sibuk
    if random.randint(1, 3) == 1:
        return {
            "status": "error",
            "message": "Server sedang sibuk"
        }

    return {
        "status": "success",
        "data": [
            {"id": 1, "name": "Ahmad"},
            {"id": 2, "name": "Budi"},
            {"id": 3, "name": "Siti"}
        ]
    }