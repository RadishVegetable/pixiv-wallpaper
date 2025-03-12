import json
from typing import List, Dict, Any


class Urls:
    """包含所有指定 size 的图片地址"""
    def __init__(self, urls: Dict[str, str])->None:
        self.urls = urls

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "Urls":
        return cls(urls=data)

    def __repr__(self) -> str:
        return json.dumps(self.urls, indent=2, ensure_ascii=False)

    def get_item(self,size='original'):
        """
        :param size: original,regular,small,thumb,mini
        :return:
        """
        return self.urls[size]

class Setu:
    """色图数据结构"""
    def __init__(self, pid: int, p: int, uid: int, title: str, author: str,
                 r18: bool, width: int, height: int, tags: List[str],
                 ext: str, aiType: int, uploadDate: int, urls: Urls) -> None:
        self.pid = pid
        self.p = p
        self.uid = uid
        self.title = title
        self.author = author
        self.r18 = r18
        self.width = width
        self.height = height
        self.tags = tags
        self.ext = ext
        self.aiType = aiType
        self.uploadDate = uploadDate
        self.urls = urls  # 这里是 Urls 类的实例

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Setu":
        """从字典解析 Setu 实例"""
        return cls(
            pid=data.get("pid", 0),
            p=data.get("p", 0),
            uid=data.get("uid", 0),
            title=data.get("title", "Unknown"),
            author=data.get("author", "Unknown"),
            r18=data.get("r18", False),
            width=data.get("width", 0),
            height=data.get("height", 0),
            tags=data.get("tags", []),
            ext=data.get("ext", ""),
            aiType=data.get("aiType", 0),
            uploadDate=data.get("uploadDate", 0),
            urls=Urls.from_dict(data.get("urls", {}))
        )

    def __repr__(self) -> str:
        return json.dumps(self.__dict__, indent=2, ensure_ascii=False)


class PixivResponse:
    """Pixiv API 响应封装类"""
    def __init__(self, error: str, data: List[Setu]) -> None:
        self.error = error
        self.data = data  # `Setu` 类的列表

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PixivResponse":
        """从 JSON 解析 PixivResponse 实例"""
        return cls(
            error=data.get("error", ""),
            data=[Setu.from_dict(item) for item in data.get("data", [])]
        )

    def __repr__(self) -> str:
        return json.dumps(self.__dict__, indent=2, ensure_ascii=False)