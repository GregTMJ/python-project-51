import codecs

from page_loader.handlers.assets_handler import handle_assets

HTML_FILE = 'fixtures/ru-hexlet-io-courses.html'
URL = 'https://ru.hexlet.io/courses'
PATH = 'ru-hexlet-io-courses_files'
ASSETS = [
    ('https://ru.hexlet.io/packs/js/runtime.js',
     'ru-hexlet-io-packs-js-runtime.js'),
    ('https://ru.hexlet.io/assets/application.css',
     'ru-hexlet-io-assets-application.css'),
    ('https://ru.hexlet.io/courses',
     'ru-hexlet-io-courses.html'),
    ('https://ru.hexlet.io/assets/professions/nodejs.png',
     'ru-hexlet-io-assets-professions-nodejs.png')
]


def read(file_path):
    with codecs.open(file_path, 'r', 'utf-8') as f:
        result = f.read()
    return result


def test_assets_handler():
    """
    Checking if the function is working correctly
    """
    html_content = read(HTML_FILE)
    _, assets = handle_assets(html_content, URL, PATH)
    assert assets == ASSETS

