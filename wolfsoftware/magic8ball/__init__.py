"""
A simple Python package to use as a template.

Attributes:
- __version__: The version of the package, retrieved from the package metadata.
- __all__: A list of all public symbols that the module exports.
"""

import importlib.metadata

from .exceptions import Magic8BallError, InvalidQuestionError
from .magic8ball import Magic8Ball

try:
    __version__: str = importlib.metadata.version('wolfsoftware.template_package_importable')
except importlib.metadata.PackageNotFoundError:
    __version__ = 'unknown'

__all__: list[str] = [
    'Magic8BallError',
    'InvalidQuestionError',
    'Magic8Ball'
]
