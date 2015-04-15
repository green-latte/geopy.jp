from setuptools import setup, find_packages
from version import VERSION

setup(
    name="geopy.jp",
    version=VERSION,
    description='Geocoding library for Python.',
    author='Green Latte',
    author_email='k.takeuchi@warrantee.co.jp',
    url='https://github.com/green-latte/geopy.jp',
    download_url=(
        'https://github.com/green-latte/geopy.jp/archive/%s.tar.gz' % VERSION
    ),
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    license='MIT',
    keywords='japan geocoding translate zipcode address',
)
