from selenium import webdriver
from .view_source import USERAGENT


def create_chrome_driver(
    chrome_exe_path: str,
    save_dir: str,
    headless: bool=True,
    disable_gpu: bool=True,
    platform: str="windows"
):
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_exe_path
    if headless:
        options.add_argument('--headless')
        options.add_argument(f"user-agent={USERAGENT[platform]}")
    if disable_gpu:
        options.add_argument('--disable-gpu')
    if platform == "linux":
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-notifications')
        options.add_argument('--enable-logging')
        options.add_argument('--v=1')
    options.add_argument('window-size=1920x1080')
    prefs = {
        "download.default_directory": save_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    return driver