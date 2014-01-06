import os
from setuptools import setup, find_packages

def slurp (fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "midi-spc-kit",
    version = "0.0.1",
    author = "softglow",
    author_email = "da.softglow@gmail.com",
    description = ("Import MIDIs to NSPC-based SNES ROMs"),
    license = "GPL v3",
    keywords = "midi spc nspc sfc rom snes music",
    url = "http://packages.python.org/midi-spc-kit",
    packages = find_packages(),
    scripts = os.listdir("scripts"),
    long_description = slurp('README.md'),
    install_requires = [
        "six >= 1.5, < 2",
    ],
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
    ],
)
