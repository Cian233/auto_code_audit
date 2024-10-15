# src/normalizers/python_normalizer.py

import ast
from .base_normalizer import BaseNormalizer
from .ir import IRNode

class PythonNormalizer(BaseNormalizer):
    """
    PythonNormalizer 用于将 Python 的 AST 转换为统一的中间表示。
    """

    def normalize(self, python_ast: ast.AST) -> IRNode:
        """
        实现对 Python AST 的规范化处理。
        :param python_ast: Python AST 对象
        :return: 统一的中间表示（IR）
        """
        ir = self._process_node(python_ast)
        return ir

    def _process_node(self, node: ast.AST) -> IRNode:
        """
        递归处理 AST 节点，转换为统一的 IR 节点。
        :param node: AST 节点
        :return: IR 节点
        """
        node_type = type(node).__name__

        # 处理不同类型的节点
        if isinstance(node, ast.Module):
            body = [self._process_node(n) for n in node.body]
            return IRNode('Module', body=body)

        elif isinstance(node, ast.FunctionDef):
            name = node.name
            args = [arg.arg for arg in node.args.args]
            body = [self._process_node(n) for n in node.body]
            return IRNode('FunctionDef', name=name, args=args, body=body)

        elif isinstance(node, ast.Assign):
            targets = [self._process_node(t) for t in node.targets]
            value = self._process_node(node.value)
            return IRNode('Assign', targets=targets, value=value)

        elif isinstance(node, ast.Expr):
            value = self._process_node(node.value)
            return IRNode('Expr', value=value)

        elif isinstance(node, ast.Call):
            func = self._process_node(node.func)
            args = [self._process_node(arg) for arg in node.args]
            return IRNode('Call', func=func, args=args)

        elif isinstance(node, ast.Name):
            return IRNode('Name', id=node.id)

        elif isinstance(node, ast.Constant):
            return IRNode('Constant', value=node.value)

        elif isinstance(node, ast.BinOp):
            left = self._process_node(node.left)
            op = type(node.op).__name__
            right = self._process_node(node.right)
            return IRNode('BinOp', left=left, op=op, right=right)

        elif isinstance(node, ast.If):
            test = self._process_node(node.test)
            body = [self._process_node(n) for n in node.body]
            orelse = [self._process_node(n) for n in node.orelse]
            return IRNode('If', test=test, body=body, orelse=orelse)

        # 处理更多的节点类型...

        else:
            # 对于未处理的节点类型，记录类型名称
            return IRNode('Unhandled', node_type=node_type)
