import requests_mock
import tempfile

from page_loader.page_loader import download, renaming_url


URL = 'https://ru.hexlet.io/courses'


def test_download():

    renaming_test_url = renaming_url(URL)
    assert renaming_test_url == "ru-hexlet-io-courses.html"

    with tempfile.TemporaryDirectory() as tempdir:
        with requests_mock.Mocker() as mock:
            mock.get(URL)
            new_path = download(URL, tempdir)
            assert new_path == f'{tempdir}\\{renaming_test_url}'
