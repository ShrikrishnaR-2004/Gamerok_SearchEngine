from flask import render_template
from app.search import search_bp

@search_bp.route("/search/voice")
def voice_search():
    return render_template("voice_search.html")
