# Glass for Markdown

## What is Glass?

A simple Python app to dynamically host a folder of
[Markdown](https://daringfireball.net/projects/markdown/) files as a
website. Any .md files placed in the `/markdown/` folder will be parsed into
HTML on the fly.

There is one non-standard Markdown feature: internal links. Double brackets 
will be parsed into links to that Markdown file: `[[example]]` in the 
Markdown becomes `<a href="/example">example</a>`. Note: Unlike some other 
implementations of this feature, files in subdirectories can only be linked to 
with the full path; to link to `/example/example`, you would type
`[[example/example]]`.

Glass also supports styling the generated HTML with CSS. Any number of
CSS stylesheets can be added by adding them to the `STYLESHEETS` list in 
`glass_config.py`, or the provided `/static/default.css` stylesheet can be 
replaced.

## Getting Started

Glass is built using Flask and Python, and should be compatible with any Flask 
compatible web sever. Setup instructions will vary by configuration and server 
host, so I can't provide them here.

If you want to run it locally for one reason or another, you would first 
download the files from this repository. Then, you'd need to [install
python](https://wiki.python.org/moin/BeginnersGuide/Download) if it isn't 
installed already. Next, you'd install Flask by following [their install
guide](https://flask.palletsprojects.com/en/3.0.x/installation/). Finally, 
Glass requires [Python-Markdown](https://python-markdown.github.io/), which
can be installed by running `pip install markdown`. Once all of that is done, 
you should be able to run `python -m flask run` in the directory you placed
Glass in and get a local webserver.