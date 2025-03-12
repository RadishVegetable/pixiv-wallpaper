from enum import Enum

class PicMode(Enum):
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    DAY_MALE = 'day_male'
    DAY_FEMALE = 'day_female'
    WEEK_ORIGINAL = 'week_original'
    WEEK_ROOKIE = 'week_rookie'
    DAY_R18 = 'day_r18'
    DAY_MALE_R18 = 'day_male_r18'
    DAY_FEMALE_R18 = 'day_female_r18'
    WEEK_R18 = 'week_r18'
    WEEK_R18G = 'week_r18g'


class WallpaperStyle(Enum):
    """
    (x,y)
    x: WallpaperStyle
    y: TileWallpaper
    """
    TILED = ('0','1')   #平铺
    CENTERED = ('0','0')    #居中
    STRETCHED = ('2','0')   #拉伸
    FIT = ('6','0') #适应
    FILL = ('10','0')   #填充
