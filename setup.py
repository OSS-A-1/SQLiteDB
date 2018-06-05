from setuptools import setup, find_packages

setup(
    name = "checkits",
    version = '1.2',
    py_modules = ['checkits'],
    author = 'hy univ. oss team a-1',
    author_email = 'suspicions@naver.com',
    url = 'https://github.com/oss-a-1/sqlitedb',
    download_url = 'https://github.com/oss-a-1/sqlitedb',
    license = 'mit license',
    keyword = ['checkit', 'checkits'],
    install_requires=['colorama', 'function'],
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
                'checkits=main.main:mainmenu_pre_login'
        ],
    },
)
