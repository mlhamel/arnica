
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='arnica',
    version='0.1',
    description='',
    long_description=long_description,
    url='https://github.com/mlhamel/arnica',
    author='Mathieu Leduc-Hamel',
    author_email='mlhamel@mlhamel.org',
    license='GPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Framework :: Scrapy',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=['']),
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points = {
        'console_scripts': [
            'arnica-crawl=arnica.scripts.crawl:main'
        ]
    },
)