#!/usr/bin/env python
from setuptools import setup

setup(name='html5slides-markdown',
      version='1.0',
      description="It's a tool to convert markdown file into slides file",
      url='https://github.com/GDG-Xian/html5slides-markdown',
      author='David Xie',
      author_email='david.scriptfan@gmail.com',
      packages=['html5slides'],
      platforms='any',
      zip_safe=False,
      install_requires=['markdown2', 'BeautifulSoup'],
      entry_points = {
            'console_scripts': ['givemeslides = html5slides.cmdline:main'],
        },
    )
