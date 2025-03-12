import os
import shutil
from typing import List, Optional, Any, IO
import time
import requests

from PicResponse import PixivResponse


# get a picture



class PixivQuery:
    def __init__(self, **kwargs) -> None:
        """
        构造函数，用于初始化请求的参数。

        支持的参数包括：
            - r18: int (0, 1, 2)
            - num: int (1-20)
            - uid: List[int]
            - keyword: str
            - tag: List[str]
            - size: List[str]
            - proxy: str
            - dateAfter: int (时间戳，单位为毫秒)
            - dateBefore: int (时间戳，单位为毫秒)
            - dsc: bool (禁用自动转换)
            - excludeAI: bool (排除 AI 作品)
            - aspectRatio: str (图片长宽比)
        """
        self.url = "https://api.lolicon.app/setu/v2"
        self.r18: Optional[int] = kwargs.get('r18', 1)  # 默认为R18
        self.num: Optional[int] = kwargs.get('num', 1)  # 默认1
        self.uid: Optional[List[int]] = kwargs.get('uid', [])
        self.keyword: Optional[str] = kwargs.get('keyword', '')
        self.tag: Optional[List[str]] = kwargs.get('tag', [])
        self.size: Optional[List[str]] = kwargs.get('size', ['original'])  # 默认图片规格 original
        self.proxy: Optional[str] = kwargs.get('proxy', 'i.pixiv.re')  # 默认反代服务
        self.dateAfter: Optional[int] = kwargs.get('dateAfter', 0)
        self.dateBefore: Optional[int] = kwargs.get('dateBefore', int(time.time() * 1000))  # 默认当前时间
        self.dsc: Optional[bool] = kwargs.get('dsc', False)  # 默认不禁用缩写转换
        self.excludeAI: Optional[bool] = kwargs.get('excludeAI', False)
        self.aspectRatio: Optional[str] = kwargs.get('aspectRatio', '')

    def to_dict(self) -> dict:
        """将对象的参数转换为字典形式"""
        return {
            'r18': self.r18,
            'num': self.num,
            'uid': self.uid,
            'keyword': self.keyword,
            'tag': self.tag,
            'size': self.size,
            'proxy': self.proxy,
            'dateAfter': self.dateAfter,
            'dateBefore': self.dateBefore,
            'dsc': self.dsc,
            'excludeAI': self.excludeAI,
            'aspectRatio': self.aspectRatio
        }

    def update_param(self, key: str, value: Any) -> None:
        if hasattr(self,key):
            setattr(self,key,value)
        else:
            raise AttributeError(f"Invalid parameter: {key}")

    def prepare_request(self) -> dict:
        return self.to_dict()

    def get_pic(self):
        params = self.to_dict()
        response = requests.get(self.url, params)
        return PixivResponse.from_dict(response.json())

    def test_url_status(self,url:str) -> bool:
        with requests.get(url, headers={"Referer": "https://app-api.pixiv.net/"}, stream=True) as response:
            if response.status_code == 200:
                return True
            else: return False

    def download(
        self,
        url: str,
        prefix: str = "",
        path: str = os.path.curdir,
        name: str | None = None,
        replace: bool = False,
        fname: str | IO[bytes] | None = None,
        referer: str = "https://app-api.pixiv.net/",
    ) -> str:
        """Download image to file (use 6.0 app-api)"""
        if hasattr(fname, "write"):
            # A file-like object has been provided.
            file = fname
        else:
            # Determine file path by parameters.
            name = prefix + str(name or fname or os.path.basename(url))
            file = os.path.join(path, name)
            if os.path.exists(file) and not replace:
                return file

        with requests.get(url, headers={"Referer": referer}, stream=True) as response:
            if isinstance(file, str):
                with open(file, "wb") as out_file:
                    shutil.copyfileobj(response.raw, out_file)
            else:
                shutil.copyfileobj(response.raw, file)  # type: ignore[arg-type]
        return file

if __name__ == '__main__':
    pq = PixivQuery()
    response = pq.get_pic()
    url = response.data[0].urls.get_item()
    print(url)
    photo_path = os.path.join(os.path.curdir, 'photo')
    print("正在下载")
    pq.download(url=url,path=photo_path)
    print("下载完成")