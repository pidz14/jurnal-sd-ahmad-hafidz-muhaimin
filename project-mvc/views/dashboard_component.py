def fetch_data_from_api(api_function):
    print("[System] Mencoba menghubungkan ke API...")

    try:
        response = api_function()

        if response["status"] == "success":
            print("[Success] Data berhasil diterima.")
            return response["data"]

        else:
            error_message = response.get(
                "message",
                "Terjadi kesalahan yang tidak diketahui"
            )

            raise Exception(error_message)

    except Exception as e:
        print(f"[Error] Gagal Integrasi: {e}")
        print("[User Info] Data tidak dapat dimuat. Silakan coba lagi nanti.")
        return None