import re

from setuptools import setup

version = ''
with open('rasa/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

config = {
    'name': 'rasa',
    'packages': ['rasa'],
    'version': version,
    'description': 'A wrapper Cisco ASA REST API',
    'author': 'Patrick Ogenstad',
    'author_email': 'patrick@ogenstad.com',
    'license': 'Apache',
    'url': 'http://networklore.com/rasa/',
    'install_requires': ['requests'],
    'classifiers': ['Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'Intended Audience :: System Administrators']
}

setup(**config)

