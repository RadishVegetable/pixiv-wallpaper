import json
import os.path
import time

from matplotlib.pyplot import title
from multipart import file_path

from ctypes_util import WallpaperSet
from lolicon_api_util import PixivQuery

if __name__ == '__main__':
    pq = PixivQuery()
    # pq.update_param("aspectRatio", 'gt1.7lt1.8')
    url = ""
    response = None
    while True:
        for i in range(10):
            print("尝试获取壁纸，第{}次".format(i + 1))
            response = pq.get_pic()
            url = response.data[0].urls.get_item()
            if pq.test_url_status(url):
                break
            else:
                print("尝试获取壁纸失败")

        print("地址正确：{}，开始下载".format(url))
        dir_path = os.path.join(os.path.abspath(os.path.curdir), 'photo')
        file_path = pq.download(url=url, path=dir_path)
        print("下载完成，标题为：{}".format(response.data[0].title))
        ws = WallpaperSet(wallpaper_path=file_path)
        ws.set_wallpaper()
        print("等待3分钟")
        time.sleep(180)




