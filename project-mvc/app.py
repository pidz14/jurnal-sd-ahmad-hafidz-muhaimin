from controllers.api_handler import get_users
from views.dashboard_component import fetch_data_from_api, render_dashboard

if __name__ == "__main__":
    # Proses Integrasi
    data = fetch_data_from_api(get_users)
    if data:
        render_dashboard(data)