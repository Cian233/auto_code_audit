# src/normalizers/__init__.py

from .base_normalizer import BaseNormalizer
from .python_normalizer import PythonNormalizer
from .java_normalizer import JavaNormalizer
from .javascript_normalizer import JavaScriptNormalizer
from .ir import IRNode

__all__ = [
    'BaseNormalizer',
    'PythonNormalizer',
    'JavaNormalizer',
    'JavaScriptNormalizer',
    'IRNode',
]
