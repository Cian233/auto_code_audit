# parsers/parser_factory.py

from .python_parser import PythonParser
from .java_parser import JavaParser
from .javascript_parser import JavaScriptParser
# 如果添加了RubyParser
# from .ruby_parser import RubyParser

class ParserFactory:
    @staticmethod
    def get_parser(language):
        """
        根据编程语言名称返回对应的解析器实例。

        参数：
            language (str): 编程语言名称。

        返回：
            BaseParser: 对应语言的解析器实例。
        """
        language = language.lower()
        if language == 'python':
            return PythonParser()
        elif language == 'java':
            return JavaParser()
        elif language == 'javascript':
            return JavaScriptParser()
        # elif language == 'ruby':
        #     return RubyParser()
        else:
            raise NotImplementedError(f"Language '{language}' is not supported.")

