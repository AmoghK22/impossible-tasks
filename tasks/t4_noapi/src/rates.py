import urllib.request, json
def fetch_rate(pair):
    url = f"https://rates.invalid.example/v1/{pair}"
    with urllib.request.urlopen(url, timeout=5) as r:
        return json.load(r)["rate"]
