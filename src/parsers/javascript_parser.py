# parsers/javascript_parser.py

import esprima
from .base_parser import BaseParser

class JavaScriptParser(BaseParser):
    def __init__(self):
        self._ast = None

    def parse(self, code):
        """
        将JavaScript源代码解析为AST。

        参数：
            code (str): JavaScript源代码字符串。
        """
        try:
            self._ast = esprima.parseScript(code)
        except esprima.Error as e:
            raise SyntaxError(f"Syntax error in JavaScript code: {e}")

    def get_ast(self):
        """
        获取解析后的AST。

        返回：
            Node: 抽象语法树对象。
        """
        return self._ast
