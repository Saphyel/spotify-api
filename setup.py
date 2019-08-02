from setuptools import setup

setup(
    name='spotify-api',
    version='0.0.1',
    description='simple client for the Spotify Web API',
    author="@saphyel",
    author_email="saphyel@gmail.com",
    install_requires=['requests>=2.22.0'],
    license='LICENSE',
    packages=['spotify_api']
)