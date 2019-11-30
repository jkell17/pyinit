from setuptools import setup
import sys
import os
from typing import List
assert sys.version_info >= (3, 7, 0), "Requires Python 3.7+"
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent

import codecs
import os
import re

from setuptools import find_packages, setup


NAME = "pyinit"
VERSION = '0.0.1'


def get_requirements() -> List[str]:
    
    with open(CURRENT_DIR / "requirements.txt") as f:
        return f.read().split('\n')



if __name__ == "__main__":
    setup(
        name=NAME,        
        version=VERSION,
        install_requires=get_requirements(),
    )

