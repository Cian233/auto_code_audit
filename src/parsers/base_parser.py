# parsers/base_parser.py

from abc import ABC, abstractmethod

class BaseParser(ABC):
    @abstractmethod
    def parse(self, code):
        pass

    @abstractmethod
    def get_ast(self):
        pass

    def parse_files(self, file_paths):
        """
        解析多个源代码文件。

        参数：
            file_paths (List[str]): 源代码文件路径列表。
        """
        asts = []
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
                self.parse(code)
                asts.append(self.get_ast())
        return asts

