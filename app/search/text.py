from flask import request, render_template
from app.search import search_bp
import requests
import os

RAWG_API_KEY = os.getenv("RAWG_API_KEY")

@search_bp.route("/search", methods=["GET", "POST"])
def search_games():
    results = []
    query = ""

    if request.method == "POST":
        query = request.form.get("query")
        url = f"https://api.rawg.io/api/games?search={query}&key={RAWG_API_KEY}"
        response = requests.get(url)

        if response.ok:
            data = response.json()
            results = data.get("results", [])

    return render_template("search.html", results=results, query=query)
