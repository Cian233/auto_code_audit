# interfaces/__init__.py

from .cli_interface import CommandLineInterface
from .web_interface import WebInterface
from .api_interface import APIInterface

__all__ = ['CommandLineInterface', 'WebInterface', 'APIInterface']
