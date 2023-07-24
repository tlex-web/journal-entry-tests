import requests


def get_holidays(country: str, year: int) -> dict | None:
    """
    Fetches all public and bank holidays from a public API.
    """
    url = f"https://date.nager.at/api/v3/publicholidays/{year}/{country}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200 and len(response.text) > 0:
            return response.json()
        else:
            return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
        return None
    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
