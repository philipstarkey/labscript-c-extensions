#####################################################################
#                                                                   #
# /__version__.py                                                   #
#                                                                   #
# Copyright 2013, Monash University                                 #
#                                                                   #
# This file is part of the program labscript-c-extensions, in the   #
# labscript suite (see http://labscriptsuite.org), and is licensed  #
# under the Simplified BSD License. See the license.txt file in the #
# root of the project for the full license.                         #
#                                                                   #
#####################################################################
import os
from pathlib import Path
try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata

VERSION_SCHEME = {
    "version_scheme": os.getenv("SCM_VERSION_SCHEME", "guess-next-dev"),
    "local_scheme": os.getenv("SCM_LOCAL_SCHEME", "node-and-date"),
}

root = Path(__file__).parent.parent
if (root / '.git').is_dir():
    from setuptools_scm import get_version
    __version__ = get_version(root, **VERSION_SCHEME)
else:
    try:
        __version__ = importlib_metadata.version(__package__)
    except importlib_metadata.PackageNotFoundError:
        __version__ = None