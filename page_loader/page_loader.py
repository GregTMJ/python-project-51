import os
import re

from page_loader.request_handler import get_content


def download(url, file_path=''):
    """
    download content from a web page and store it locally
    :param url: the web page
    :param file_path: the directory where the content will be downloaded
    :return: directory name
    """
    full_file_path = os.path.join(os.getcwd(), file_path)
    renamed_url: str = renaming_url(url)
    html_content_file_path: str = renamed_url + '_files'
    html_file_name: str = renamed_url + '.html'
    html_file_path: str = os.path.join(full_file_path, html_file_name)
    data = get_content(url)
    # with open(new_web_file_name, 'w') as file:
    #     file.write(data)
    content_file_path = os.path.join(full_file_path, html_content_file_path)
    return html_file_path


def renaming_url(url: str) -> str:
    """
    helps rename files
    :param url: the web request
    :return: new name
    """
    if 'https://' in url:
        url = re.sub(r"https://", '', url)
    return re.sub(r"(\.)|(/)", "-", url)
