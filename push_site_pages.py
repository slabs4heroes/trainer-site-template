import requests, sys
from urllib.parse import urlencode

BASE = sys.argv[1]
ADMIN_KEY = "eMtUzm1ORic7Zqi6IiSafXVb6qg3yHex"
CLIENT_ID = "475c7b73-8e0a-4977-93c2-2073b205c934"
BUSINESS_NAME = "Gator Alley Dog Training Academy, LLC"

PAGES = ["home", "programs", "about", "contact"]

for page in PAGES:
    html = open(f"/work/temp/gen_out/{page}.html", encoding="utf-8").read()
    qs = urlencode({"clientId": CLIENT_ID, "page": page, "businessName": BUSINESS_NAME})
    r = requests.post(
        f"{BASE}/admin/site-pages?{qs}",
        headers={"x-admin-key": ADMIN_KEY, "Content-Type": "text/html"},
        data=html.encode("utf-8"),
        timeout=30,
    )
    print(page, r.status_code, r.text[:200])
