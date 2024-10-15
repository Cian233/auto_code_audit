# parsers/java_parser.py

import javalang
from .base_parser import BaseParser

class JavaParser(BaseParser):
    def __init__(self):
        self._ast = None

    def parse(self, code):
        """
        将Java源代码解析为AST。

        参数：
            code (str): Java源代码字符串。
        """
        try:
            self._ast = javalang.parse.parse(code)
        except javalang.parser.JavaSyntaxError as e:
            raise SyntaxError(f"Syntax error in Java code: {e}")

    def get_ast(self):
        """
        获取解析后的AST。

        返回：
            Node: 抽象语法树对象。
        """
        return self._ast
