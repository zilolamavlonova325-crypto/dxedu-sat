from flask import Response
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/math")
def math():
    return render_template("math.html")

@app.route("/english")
def english():
    return render_template("english.html")
@app.route("/sitemap.xml")
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://dxedu-sat.onrender.com/</loc>
    </url>
    <url>
        <loc>https://dxedu-sat.onrender.com/math</loc>
    </url>
    <url>
        <loc>https://dxedu-sat.onrender.com/english</loc>
    </url>
</urlset>"""
    return Response(xml, mimetype="application/xml")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
