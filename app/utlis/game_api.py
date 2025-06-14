import os
import requests

RAWG_API_KEY = os.getenv("RAWG_API_KEY", "your_rawg_api_key")

def search_games(query, page=1):
    """Search games from RAWG API"""
    url = f"https://api.rawg.io/api/games"
    params = {
        "key": RAWG_API_KEY,
        "search": query,
        "page": page
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        return []

def get_game_details(game_id):
    """Get detailed info of a game"""
    url = f"https://api.rawg.io/api/games/{game_id}"
    params = {"key": RAWG_API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {}
