import os
import shutil
from tqdm import tqdm
from datetime import datetime
from bs4 import BeautifulSoup
from vidfetch.video import VideoDataset, VideoData
from vidfetch.utils import download_view_source, download, get_md5
from vidfetch.uid.mixkit import generate_mixkit_video_uid,  CATEGORY_PAGE_NUM
from selenium.webdriver.chrome.webdriver import WebDriver


class MixkitVideoDataset(VideoDataset):
    def __init__(self, root_dir: str):
        super().__init__(
            website="mixkit", 
            root_dir=root_dir
        )
    
    def download(
        self, 
        platform: str="windows",
    ):
        for category, page_num in CATEGORY_PAGE_NUM.items():
            print(f"download the {category} with {page_num} pages")
            for page_idx in tqdm(range(page_num)):
                self.download_with_category_page_idx(
                    category=category,
                    page_idx=page_idx+1,
                    platform=platform
                )

    def download_with_category_page_idx(
        self,
        category: str, 
        page_idx: int,
        platform: str,
    ):
        # download view source
        fetch_page_url = f"https://mixkit.co/free-stock-video/{category}/?page={page_idx}"
        view_source_download_path = os.path.join(self.cache_dir, f"{category}_{page_idx}.html")
        if not os.path.exists(view_source_download_path):
            download_view_source(
                website="mixkit",
                url=fetch_page_url,
                save_path=view_source_download_path,
                platform=platform
            )
        
        # read data from html
        with open(view_source_download_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        # unprocess download url
        html_unprocess_download_urls = soup.find_all(class_="item-grid-video-player__video-wrapper")
        unprocess_download_urls = [video.find('video')['src'] for video in html_unprocess_download_urls]
        # text and origin url
        html_origin_urls = soup.find_all(class_="item-grid-card__title")
        origin_urls = ["https://mixkit.co" + video.find('a')['href'] for video in html_origin_urls]
        
        for idx, unprocess_download_url in tqdm(enumerate(unprocess_download_urls)):
            # download the origin page's view source
            origin_url = origin_urls[idx]
            origin_url_download_path = os.path.join(self.cache_dir, f"{category}_{page_idx}_{idx}.html")
            if not os.path.exists(origin_url_download_path):
                download_view_source(
                    website="mixkit",
                    url=origin_url,
                    save_path=origin_url_download_path ,
                    platform=platform
                )
            # read data from html
            with open(origin_url_download_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            owner = soup.find(class_="item-page__contributor-link")['href'][1: -1]    
            name = soup.find(class_="item-page__title").text
            text = soup.find(class_="item-page__description").text
            highest_str_resolution = soup.find_all(class_="video-item__download-label")[-1].text
            resolution = '4k' if '4K' in highest_str_resolution else '1080p'
            
            # process the unprocess_download_url
            unprocess_download_url: str
            download_url = unprocess_download_url.replace("/preview/", "/download/")
            if resolution == '4k':
                download_url = download_url.replace("-small", "-4k")
            else:
                download_url = download_url.replace("-small", "-1080")

            # check if is downloaded sucessfully 
            if download_url in self.monitor.downloaded_url_list:
                continue
            
            # download
            download_success = True
            tmp_filename =  f"{category}_{page_idx}_{idx}_tmp.mp4"
            tmp_download_path = os.path.join(self.tmp_dir, tmp_filename)
            try:
                download(tmp_download_path, download_url)
            except:
                download_success = False
                cur_time = str(datetime.now())
                error_message = f"{cur_time}: error occurred when the download url is {download_url}"
                with open(self.log_path, "a") as log_file:
                    log_file.write(error_message)
            if not download_success:
                continue
            
            # if download sucessfully, record the info of video
            md5 = get_md5(tmp_download_path)
            uid = generate_mixkit_video_uid(
                category=category,
                page_idx=page_idx,
                inner_idx=idx,
                md5=md5
            )
            save_path = os.path.join(self.download_dir, f"{uid}.mp4")
            shutil.move(tmp_download_path, save_path)
            
            video_info_dict = {
                "uid": uid,
                "name": name,
                "text": text,
                "free": True,
                "owner": owner,
                "save_path": save_path,
                "website": self.website,
                "origin_url": origin_url,
                "download_url": download_url,
                "resolution": resolution,
            }
            
            video_data = VideoData(
                video_info_dict=video_info_dict,
                basic_info_include=False
            )
            new_video_info_dict = video_data.get_video_info_dict()
            self.monitor.add_item(new_video_info_dict)
            self.monitor.update_state()
            self.monitor.save_state_dict()
            
            