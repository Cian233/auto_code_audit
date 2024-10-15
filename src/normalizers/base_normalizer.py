# src/normalizers/base_normalizer.py

from abc import ABC, abstractmethod
from typing import Any
from .ir import IRNode

class BaseNormalizer(ABC):
    """
    BaseNormalizer 定义了规范化器的接口。
    所有具体的规范化器都需要继承此类并实现其中的方法。
    """

    @abstractmethod
    def normalize(self, ast: Any) -> IRNode:
        """
        将语言特定的 AST 转换为统一的中间表示（IR）。
        :param ast: 语言特定的 AST 对象
        :return: 统一的中间表示（IR）
        """
        pass
