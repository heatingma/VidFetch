import os
import shutil
from vidfetch.api.huggingface import pull_from_hf
from vidfetch.utils import extract_archive


def youtube_dl_install_helper(
    hf_token: str,
):
    # download youtube-dl-2024.04.08.tar.gz
    pull_from_hf(
        hf_token=hf_token,
        hf_repo_id="OpenVideo/Panda-70M-Original-Links",
        filename="youtube-dl-2024.04.08.tar.gz",
        save_dir="./"
    )
    
    # extract_archive the youtube-dl-2024.04.08.tar.gz
    extract_archive(
        archive_path="youtube-dl-2024.04.08.tar.gz",
        extract_path="youtube-dl-2024.04.08"
    )
    
    # build dist package
    ori_dir = os.getcwd()
    os.chdir("youtube-dl-2024.04.08/youtube-dl")
    os.system("python setup.py sdist")
    os.chdir(ori_dir)
    
    # pip install youtube_dl-2024.4.8.tar.gz
    ori_dir = os.getcwd()
    os.chdir("youtube-dl-2024.04.08/youtube-dl/dist")
    os.system("pip install youtube_dl-2024.4.8.tar.gz")
    os.chdir(ori_dir)
    
    # remove the package
    os.remove("youtube-dl-2024.04.08.tar.gz")
    shutil.rmtree("youtube-dl-2024.04.08")