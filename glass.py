from flask import abort, url_for
from markdown import markdown
import glass_config as CONFIG
import re

def get_doctype():
    return "<!DOCTYPE html>"

def get_head(title):
    output = []
    output.append("<head>")
    output.append(f"<title>{title}</title>")

    for stylesheet in CONFIG.STYLESHEETS:
        # Stylesheets starting with http are treated as externally hosted.
        # Those without this are assumed to be in /static/styles/
        if(stylesheet[:4] == "http"):
            url = stylesheet
        else:
            url = url_for("static", filename=f"styles/{stylesheet}")
        output.append(f"<link rel=\"stylesheet\" href=\"{url}\">")

    output.append("</head>")
    return "\n".join(output)

def get_markdown(id):
    path = f"{CONFIG.MARKDOWN_DIRECTORY}/{id}.md"
    print(path)
    try:
        file = open(path, "r")
    except FileNotFoundError:
        return abort(404)
    except:
        return abort(500)
    
    return file.read()

def generate_page(id):
    # First, get the parsed markdown of the article.
    body = markdown(get_markdown(id))

    # Find the first h1 tag and use its contents as the title.
    title_start = body.find("<h1>")
    title_end = body.find("</h1>")
    title = body[title_start + 4:title_end]

    # Special Case: [[DEFAULT_FILE]] should link to /
    body = body.replace(f"[[{CONFIG.DEFAULT_FILE}]]", f"<a href=\"/\">{CONFIG.DEFAULT_FILE}</a>")

    # Parse for any [[]] links using a regex and replace with <a> tags
    body = re.sub(r'\[\[([^\s]+)\]\]', r'<a href="/\1">\1</a>', body)

    # Generate a complete HTML page.
    output = []
    output.append(get_doctype())
    output.append(get_head(title))
    output.append("<body>")
    output.append(body)
    output.append("</body>")
    output.append("</html>")

    return "\n".join(output)