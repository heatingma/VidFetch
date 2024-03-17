import os
import hashlib
import time
import shutil
import asyncio
import aiohttp
import requests
import async_timeout
import urllib.request
from tqdm import tqdm
from texttable import Texttable


def check_url_exists(url):
    try:
        response = requests.head(url)
        return response.status_code == requests.codes.ok
    except requests.exceptions.RequestException:
        return False


def download(filename: str, url: str, md5: str=None, retries: int=5):
    if type(url) == str:
        return _download(filename, url, md5, retries)
    elif type(url) == list:
        for cur_url in url:
            try:
                return _download(filename, cur_url, md5, retries)
            except RuntimeError:
                continue
        raise RuntimeError('Max Retries exceeded!')
    else:
        raise ValueError("The url should be string or list of string.")

  
def _download(filename: str, url: str, md5: str, retries):
    if retries <= 0:
        raise RuntimeError('Max Retries exceeded!')

    if not os.path.exists(filename):
        if retries % 3 == 2:
            try:
                down_res = requests.get(url, stream=True)
                file_size = int(down_res.headers.get('Content-Length', 0))
                with tqdm.wrapattr(down_res.raw, "read", total=file_size) as content:
                    with open(filename, 'wb') as file:
                        shutil.copyfileobj(content, file)
            except requests.exceptions.ConnectionError as err:
                return download(filename, url, md5, retries - 1)
        elif retries % 3 == 1:
            try:
                asyncio.run(_asyncdownload(filename, url))
            except:
                return _download(filename, url, md5, retries - 1)
        else:
            try:
                urllib.request.urlretrieve(url, filename)
            except:
                return _download(filename, url, md5, retries - 1)
            
    if md5 is not None:
        md5_returned = get_md5(filename)
        if md5 != md5_returned:
            os.remove(filename)
            time.sleep(1)
            return _download(filename, url, md5, retries - 1)
    return filename


async def _asyncdownload(filename: str, url: str):
    async with aiohttp.ClientSession() as session:
        async with async_timeout.timeout(120):
            async with session.get(url) as response:
                with open(filename, 'wb') as file:
                    async for data in response.content.iter_chunked(512):
                        file.write(data)


def get_md5(filename: str):
    hash_md5 = hashlib.md5()
    chunk = 8192
    with open(filename, 'rb') as file_to_check:
        while True:
            buffer = file_to_check.read(chunk)
            if not buffer:
                break
            hash_md5.update(buffer)
        md5_returned = hash_md5.hexdigest()
        return md5_returned
    

def print_dict_as_table(data_dict):
    """
    Prints the contents of a dictionary as a table, with each key-value pair in a separate row.

    Args:
    data_dict (dict): The dictionary to be printed as a table.
    """
    # Create a new Texttable object
    table = Texttable()
    # Set the table header
    table.header(["Key", "Value"])
    # Iterate through the dictionary and add each key-value pair to the table
    for key, value in data_dict.items():
        table.add_row([key, value])
    # Print the table
    print(table.draw())
