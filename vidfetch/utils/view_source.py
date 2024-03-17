import requests


USERAGENT = {
    "windows": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "mac": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "linux": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}


REFER = {
    "mixkit": "https://mixkit.co",
    "pixabay": "https://pixabay.com/videos/search/?order=ec"
}


def download_view_source(
    website: str,
    url: str,
    save_path: str,
    platform: str="windows"
):
    headers = {
        "User-Agent": USERAGENT[platform],
        "referer": REFER[website]
    }
    res = requests.get(url, headers=headers)
    with open(save_path, 'w', encoding='utf-8') as file:
        file.write(res.text)