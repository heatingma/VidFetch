from vidfetch.website import MixkitVideoDataset

mixkit = MixkitVideoDataset(root_dir="mixkit")
mixkit.download(platform="windows")
