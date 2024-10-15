# src/machine_learning/model_interface.py

from abc import ABC, abstractmethod
from typing import List, Dict

class ModelInterface(ABC):
    """
    机器学习模型的接口，定义了分析代码的方法。
    """

    @abstractmethod
    def analyze_code(self, code_snippet: str, language: str) -> List[Dict]:
        """
        分析给定的代码片段，返回潜在的漏洞信息。

        Args:
            code_snippet (str): 要分析的代码片段。
            language (str): 代码的编程语言。

        Returns:
            List[Dict]: 检测到的漏洞列表，每个漏洞用字典表示。
        """
        pass
