def fetch_data_from_api(api_function):
    print("[System] Mencoba menghubungkan ke API...")
    try:
        response = api_function()
        if response["status"] == "success":
            return response["data"]
        else:
            raise Exception("API Return Error")
    except Exception as e:
        print(f"[Error] Gagal Integrasi: {e}")
        return None