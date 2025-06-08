from flask import render_template
from app.search import search_bp

@search_bp.route("/search/image")
def image_search():
    return render_template("image_search.html")
