# parsers/python_parser.py

import ast
from .base_parser import BaseParser

class PythonParser(BaseParser):
    def __init__(self):
        self._ast = None

    def parse(self, code):
        """
        将Python源代码解析为AST。

        参数：
            code (str): Python源代码字符串。
        """
        try:
            self._ast = ast.parse(code)
        except SyntaxError as e:
            raise SyntaxError(f"Syntax error in Python code: {e}")

    def get_ast(self):
        """
        获取解析后的AST。

        返回：
            ast.AST: 抽象语法树对象。
        """
        return self._ast
