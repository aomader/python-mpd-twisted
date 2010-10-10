#!/usr/bin/env python

from setuptools import setup

DESCRIPTION = """\
An MPD (Music Player Daemon) client library written in pure Python, using Twisted
"""

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

LICENSE = """\
Copyright (C) 2008  J. Alexander Treuman <jat@spatialrift.net>
Copyright (C) 2010  Jasper St. Pierre <jstpierre@mecheye.net>
Copyright (C) 2010  Oliver Mader <b52@reaktor42.de>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

setup(
    name="python-mpd-twisted",
    version="0.3.0",
    description="Python MPD client library using Twisted",
    long_description=DESCRIPTION,
    author="J. Alexander Treuman, JP St. Pierre, Oliver Mader",
    author_email="jat@spatialrift.net, jstpierre@mecheye.net, b52@reaktor42.de",
    maintainer="Oliver Mader",
    maintainer_email="b52@reaktor42.de",
    url="https://code.reaktor42.de/projects/python-mpd-twisted",
    download_url="https://code.reaktor42.de/projects/python-mpd-twisted",
    py_modules=["mpd"],
    classifiers=CLASSIFIERS,
    license=LICENSE,
    keywords=["mpd"],
    platforms=["Independant"],
    install_requires=["twisted>=10.1.0"]
)

# vim: set expandtab shiftwidth=4 softtabstop=4 textwidth=79:
