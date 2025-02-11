import json
import os.path
from datetime import datetime,timedelta
from PicMode import PicMode
from pixiv_auth import login
from pixivpy3 import AppPixivAPI
import re

# access_token,refresh_token = login()
#
# data = {
#     "access_token":access_token,
#     "refresh_token":refresh_token
# }
# with open('config.json', 'w', encoding='utf-8') as f:
#     json.dump(data,f, ensure_ascii=False, indent=4)


current_time = datetime.now()
current_date = current_time.date().strftime("%Y-%m-%d")
yesterday_date = (current_time - timedelta(days=1)).strftime("%Y-%m-%d")


with open('config.json', 'r', encoding='utf-8') as file:
    token = json.load(file)

api = AppPixivAPI()

api.set_auth(token['access_token'], token['refresh_token'])


photo_path = os.path.join(os.path.curdir,'photo',yesterday_date)
if not os.path.exists(photo_path):
    os.mkdir(photo_path)


json_result = api.illust_ranking(PicMode.DAY_R18.value, date=yesterday_date)

i = 0
for illust in json_result.illusts:

    i+=1
    id = illust.id
    print(f'''index:{i}, {id} is downloading, title = {illust.title}''')
    origin_url=illust.meta_single_page.original_image_url

    if origin_url is not None:
        api.download(url=origin_url, path=photo_path)
    else:
        # 套图
        meta_pages = illust.meta_pages
        j = 0
        for mp in meta_pages:
            origin_url = mp.image_urls.original
            print(f'''index:{i}, {id} is downloading,sub id is {os.path.basename(origin_url)}, title = {illust.title}''')
            api.download(url=origin_url, path=photo_path)
            j+=1

print("ok")

