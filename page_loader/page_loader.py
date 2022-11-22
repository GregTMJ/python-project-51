import os
import re
import requests


def download(web_path, file_path=os.getcwd()):
    """
    download content from a web page and store it locally
    :param web_path: the web page
    :param file_path: the directory where the content will be downloaded
    :return: directory name
    """
    path = os.path.join(file_path)
    new_web_file_name: str = renaming_url(web_path)
    new_web_path_name: str = os.path.join(path, new_web_file_name)
    data = get_content(web_path)
    # with open(new_web_file_name, 'wb') as file:
    #     file.write(data)
    return new_web_path_name


def renaming_url(url: str) -> str:
    """
    helps rename files
    :param url: the web request
    :return: new name
    """
    if 'https://' in url:
        url = re.sub(r"https://", '', url)
    return re.sub(r"(\.)|(/)", "-", url) + '.html'


def get_content(url: str) -> bytes:
    """
    download content from url
    :param url: the given url
    :return: the request results
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.content
