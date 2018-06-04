from setuptools import setup, find_package

setup(
    name = "checkits",
    version = '1.01',
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
                'checkits=main:mainmenu_pre_login'
        ],
    },
)
