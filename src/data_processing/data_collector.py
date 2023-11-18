import requests

def fetch_energy_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data")

# Example usage
# data = fetch_energy_data('API_ENDPOINT_URL')
