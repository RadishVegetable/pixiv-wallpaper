
from pixiv_auth import login
from pixivpy3 import AppPixivAPI

access_token,refresh_token = login()

api = AppPixivAPI()
api.set_auth(access_token, refresh_token)

json_result = api.illust_ranking('day', date='2025-02-01')
print(json_result)
illust = json_result.illusts[0]
print(f">>> {illust.title}, origin url: {illust.image_urls.large}")


