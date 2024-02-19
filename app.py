from flask import Flask, abort, redirect
from glass import generate_page
from glass_config import DEFAULT_FILE

app = Flask(__name__)

@app.route("/")
def root():
    return generate_page(DEFAULT_FILE)

@app.route("/<path:article_id>")
def article(article_id):
    # Stop path traversal attack.
    if ".." in article_id:
        abort(401)
    
    return generate_page(article_id)
