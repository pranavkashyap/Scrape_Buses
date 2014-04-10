try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Bus Scraper',
    'author': 'Pranav Kashyap',
    'url': 'TBD',
    'download_url': 'TBD',
    'author_email': 'pranavk@wharton.upenn.edu',
    'install_requires': ['nose'],
    'version': '0.1',
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Bus Aggregator'
}

setup(**config)