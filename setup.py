#!/usr/bin/env python

from setuptools import setup

DESCRIPTION = """\
An MPD (Music Player Daemon) client library written in pure Python, using 
Twisted
"""

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules"
]

setup(
    name="python-mpd-twisted",
    version="0.4",
    description="Python MPD client library using Twisted",
    long_description="An MPD (Music Player Daemon) client library, written " \
                     "in pure Python, using Twisted",
    author="J. Alexander Treuman, Jasper St. Pierre, Oliver Mader",
    author_email="jat@spatialrift.net, jstpierre@mecheye.net, " \
                  "b52@reaktor42.de",
    maintainer="Oliver Mader",
    maintainer_email="b52@reaktor42.de",
    url="https://code.reaktor42.de/projects/python-mpd-twisted",
    download_url="http://pypi.python.org/pypi/python-mpd-twisted",
    py_modules=["mpd"],
    classifiers=CLASSIFIERS,
    license="GPL3",
    keywords=["mpd"],
    platforms=["Independent"],
    install_requires=["Twisted>=10.1.0"]
)

# vim: set expandtab shiftwidth=4 softtabstop=4 textwidth=79:
