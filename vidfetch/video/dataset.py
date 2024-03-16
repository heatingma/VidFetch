import os
from .monitor import VideoMonitor
from vidfetch.utils import print_dict_as_table


class VideoDataset:
    def __init__(
        self, 
        website: str,
        root_dir: str
    ):
        self.website = website
        self.root_dir = root_dir
        self.download_dir = os.path.join(root_dir, "download")
        self.tmp_dir = os.path.join(root_dir, "tmp")
        self.cache_dir = os.path.join(root_dir, "cache")
        self.log_path = os.path.join(root_dir, "run_log.txt")
        self.monitor_save_path = os.path.join(root_dir, "monitor.npy")
        # check dir
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
        # monitor
        self.monitor = VideoMonitor(
            save_path=self.monitor_save_path,
            website=website
        )
        # read from videos_state_dict
        self.monitor.load_state()
        videos_state_dict = self.monitor.videos_state_dict
        if videos_state_dict['last_video'] == dict():
            print("You haven't downloaded any video.")
        else:
            last_video = videos_state_dict['last_video']
            print(f"Last save time: {videos_state_dict['last_save_time']}")
            print(f"Summary is as followed")
            print_dict_as_table(videos_state_dict['summary'])
            print(f"The last video you have download is as followed.")
            print_dict_as_table(last_video)

    def download(
        self, 
        platform: str="windows"
    ):
        raise NotImplementedError()
    
    def __repr__(self) -> str:
        f"{self.__class__.__name__}({self.website})"  