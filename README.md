# Turtle War

```
Turtle War-это игра-убивалка веремени, цель которой не столкнуться c ботом
```


# Сайт

<a href='http://vlahouse.ru/projects/tw/'>http://vlahouse.ru/projects/tw/</a>


# Install

#### Whl install
```sh
wget https://github.com/CharlesPikachu/Games/releases/download/v0.1.2/cpgames-0.1.2-py3-none-any.whl
pip install cpgames-0.1.2-py3-none-any.whl
```

#### Pip install
```
run "pip install cpgames"
```

#### Source code install
```sh
(1) Offline
Step1: git clone https://github.com/CharlesPikachu/Games.git
Step2: cd Games -> run "python setup.py install"
(2) Online
run "pip install git+https://github.com/CharlesPikachu/Games.git@master"
```


# Quick Start
```python
import random
from cpgames import cpgames

game_client = cpgames.CPGames()
all_supports = game_client.getallsupported()
game_client.execute(random.choice(list(all_supports.values())))
```


# Screenshot
![img](./docs/screenshot.gif)


# Projects in Charles_pikachu
- [Games](https://github.com/CharlesPikachu/Games): Create interesting games in pure python.
- [DecryptLogin](https://github.com/CharlesPikachu/DecryptLogin): APIs for loginning some websites by using requests.
- [Musicdl](https://github.com/CharlesPikachu/musicdl): A lightweight music downloader written in pure python.
- [Videodl](https://github.com/CharlesPikachu/videodl): A lightweight video downloader written in pure python.
- [Pytools](https://github.com/CharlesPikachu/pytools): Some useful tools written in pure python.
- [PikachuWeChat](https://github.com/CharlesPikachu/pikachuwechat): Play WeChat with itchat-uos.
- [Pydrawing](https://github.com/CharlesPikachu/pydrawing): Beautify your image or video.
- [ImageCompressor](https://github.com/CharlesPikachu/imagecompressor): Image compressors written in pure python.
- [FreeProxy](https://github.com/CharlesPikachu/freeproxy): Collecting free proxies from internet.
- [Paperdl](https://github.com/CharlesPikachu/paperdl): Search and download paper from specific websites.
- [Sciogovterminal](https://github.com/CharlesPikachu/sciogovterminal): Browse "The State Council Information Office of the People's Republic of China" in the terminal.
- [CodeFree](https://github.com/CharlesPikachu/codefree): Make no code a reality.
- [DeepLearningToys](https://github.com/CharlesPikachu/deeplearningtoys): Some deep learning toys implemented in pytorch.
- [DataAnalysis](https://github.com/CharlesPikachu/dataanalysis): Some data analysis projects in charles_pikachu.
- [Imagedl](https://github.com/CharlesPikachu/imagedl): Search and download images from specific websites.
- [Pytoydl](https://github.com/CharlesPikachu/pytoydl): A toy deep learning framework built upon numpy.
- [NovelDL](https://github.com/CharlesPikachu/noveldl): Search and download novels from some specific websites.


# Citation
If you use this project in your research, please cite this project.
```
@misc{games2020,
    author = {Zhenchao Jin},
    title = {Games: Create interesting games in pure python},
    year = {2020},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/CharlesPikachu/Games}},
}
```


# More

#### WeChat Official Accounts
*Charles_pikachu*  
![img](./docs/pikachu.jpg)