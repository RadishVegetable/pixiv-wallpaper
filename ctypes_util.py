import ctypes
import winreg
from typing import Optional

import win32api
import os

from pixiv_enum import WallpaperStyle


# 使用 Windows API 设置壁纸
class WallpaperSet:
    def __init__(self,wallpaper_style= WallpaperStyle.FIT,wallpaper_path=""):
        self.wallpaper_style = wallpaper_style
        self.wallpaper_path =wallpaper_path

    def update_wallpaper_style(self,wallpaper_style):
        if self.wallpaper_style != wallpaper_style:
            self.wallpaper_style = wallpaper_style
            self.set_wallpaper_style()


    def set_wallpaper_style(self):
        key_path = r"Control Panel\Desktop"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, self.wallpaper_style.value[1])  # 1 = 平铺，0 = 关闭平铺
            winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, self.wallpaper_style.value[0])  # 0 = 居中（配合 TileWallpaper 才有效）

    def update_wallpaper_path(self,wallpaper_path):
        self.wallpaper_path = wallpaper_path
        self.set_wallpaper()

    def set_wallpaper(self):
        self.set_wallpaper_style()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.wallpaper_path, 3)