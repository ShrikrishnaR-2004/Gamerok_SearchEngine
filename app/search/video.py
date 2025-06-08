from flask import render_template
from app.search import search_bp

@search_bp.route("/search/video")
def video_search():
    return render_template("video_search.html")
