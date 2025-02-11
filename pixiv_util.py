
from pixivpy3.aapi import AppPixivAPI



def download(url, destination, referer='https://app-api.pixiv.net/'):
    """
    Download a file to a given destination. This method uses
    the client's access token if available.

    :param str url:     The URL of the file.
    :param destination: The destination file. Must be writeable.
    :param str referer: The Referer header.

    :raises FileNotFoundError: If the destination's directory does
        not exist.
    :raises PermissionError: If the destination cannot be written to.
    """
    AppPixivAPI.download()
    response = AppPixivAPI.no_auth_requests_call(url=url, headers={"Referer": referer}, stream=True)
    with destination.open("wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)