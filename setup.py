from rasa import __version__
from rasa import __author__
from setuptools import setup

config = {
    'name': 'rasa',
    'packages': ['rasa'],
    'version': __version__,
    'description': 'A wrapper Cisco ASA REST API',
    'author': __author__,
    'author_email': 'patrick@ogenstad.com',
    'license': 'Apache',
    'url': 'http://networklore.com/rasa/',
    'install_requires': ['requests'],
    'classifiers': ['Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'Intended Audience :: System Administrators']
}

setup(**config)

