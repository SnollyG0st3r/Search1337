from setuptools import setup


setup(
    name = "cmdline-search1337",
    packages = ["1337"],
    entry_points={
        'console_scripts': [
            'search1337 = 1337.call:main',
        ]
    },
    
    install_requires=[
            "bs4",
            "mechanize",
        ],



    version = "0.2",
    description = "Online, lightweight exploit scanner and downloader.",
    author = "B3mB4m",
    author_email = "b3mb4m@protonmail.com",
    )
