import http.server
import json
import os
import socketserver
import urllib.parse

PORT = 8001
ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES_DIR = os.path.join(ROOT, "pages")
INDEX_FILE = os.path.join(ROOT, "pages-index.json")


def generate_pages_index():
    files = []
    for dirpath, _dirnames, filenames in os.walk(PAGES_DIR):
        for name in filenames:
            if name.lower().endswith(".md"):
                rel = os.path.relpath(os.path.join(dirpath, name), PAGES_DIR)
                files.append(rel.replace(os.sep, "/"))
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(files), f, ensure_ascii=False, indent=2)


def inject_base_href():
    for name in ("index.html", "404.html"):
        path = os.path.join(ROOT, name)
        if not os.path.isfile(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("%BASE_PATH%", "/")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)


class SpaHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(parsed.path)
        fs_path = os.path.join(ROOT, path.lstrip("/"))

        if os.path.isfile(fs_path):
            return super().do_GET()

        self.path = "/index.html"
        return super().do_GET()


generate_pages_index()
inject_base_href()

with socketserver.TCPServer(("", PORT), SpaHandler) as httpd:
    print(f"Serving on http://127.0.0.1:{PORT}")
    httpd.serve_forever()