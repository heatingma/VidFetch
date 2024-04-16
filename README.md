<div align="center">
<img src="static/logo-2.png" alt="logo" width="750"/>
</div>

[![PyPi version](https://badgen.net/pypi/v/vidfetch/)](https://pypi.org/pypi/vidfetch/) [![PyPI pyversions](https://img.shields.io/badge/dynamic/json?color=blue&label=python&query=info.requires_python&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fvidfetch%2Fjson)](https://pypi.python.org/pypi/vidfetch/) [![Downloads](https://static.pepy.tech/badge/vidfetch)](https://pepy.tech/project/vidfetch) [![GitHub stars](https://img.shields.io/github/stars/heatingma/VidFetch.svg?style=social&label=Star&maxAge=8640)](https://GitHub.com/heatingma/VidFetch/stargazers/) 

``Latte``, **a novel latent diffusion transformer for video generation**, utilizes spatio-temporal tokens extracted from input videos and employs a series of Transformer blocks to model the distribution of videos in the latent space. ``Latte`` achieves state-of-the-art performance on four standard video generation datasets ``FaceForensics``, ``SkyTimelapse``, ``UCF101``, and ``Taichi-HD``. [paper](https://arxiv.org/pdf/2401.03048v1.pdf), [code](https://github.com/Vchitect/Latte?tab=readme-ov-file), [pretrained](https://huggingface.co/maxin-cn/Latte)


However, ``Latte`` still falls short in terms of video generation length and quality compared to ``Sora``. To achieve training and generation effects close to Sora, the Latte model requires more high-quality text-video paired datasets. Therefore, we have created ``VidFetch``, an open-source dataset download tool to obtain copyright-free videos from various free video websites.


## Free Video Support

| website | windows | macos | linux |
| :-----: | :-----: | :---: | :---: |
| [Pexels](https://www.pexels.com) | ✔ | 📆 | 📆 |
| [Mazwai](https://mazwai.com/stock-video-footage) | 📆 | 📆 | 📆 |
| [Mixkit](https://mixkit.co/free-stock-video) | ✔ | 📆 | ✔ |
| [Pixabay](https://pixabay.com/videos/search/?order=ec) | ✔ | 📆 | 📆 |
| [Coverr](https://coverr.co/stock-video-footage) | 📆 | 📆 | 📆 |

## Installation

You can install the stable release on PyPI:

```bash
$ pip install vidfetch
```

or get the latest version by running:

```bash
$ pip install -U https://github.com/heatingma/VidFetch/archive/master.zip # with --user for user install (no root)
```

The following packages are required, and shall be automatically installed by ``pip``:

```
aiohttp>=3.9.3,
async_timeout>=4.0.3
tqdm>=4.66.2
texttable>=1.7.0
moviepy>=1.0.3
bs4>=0.0.2
selenium>=4.18.1
requests>=2.31.0
texttable>=1.7.0
huggingface_hub>=0.22.2
```

## Usage Examples

### website

**You only need three lines of code to start downloading the video**
```python
from vidfetch.website import MixkitVideoDataset

mixkit = MixkitVideoDataset(root_dir="mixkit")
mixkit.download(platform="windows")
```
