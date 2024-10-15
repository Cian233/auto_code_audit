# src/normalizers/javascript_normalizer.py

from .base_normalizer import BaseNormalizer
from .ir import IRNode

class JavaScriptNormalizer(BaseNormalizer):
    """
    JavaScriptNormalizer 用于将 JavaScript 的 AST 转换为统一的中间表示。
    """

    def normalize(self, js_ast: dict) -> IRNode:
        """
        实现对 JavaScript AST 的规范化处理。
        :param js_ast: JavaScript AST 对象（通常是字典形式）
        :return: 统一的中间表示（IR）
        """
        ir = self._process_node(js_ast)
        return ir

    def _process_node(self, node: dict) -> IRNode:
        """
        递归处理 AST 节点，转换为统一的 IR 节点。
        :param node: AST 节点（字典）
        :return: IR 节点
        """
        node_type = node.get('type', 'Unknown')

        # 处理不同类型的节点
        if node_type == 'Program':
            body = [self._process_node(n) for n in node.get('body', [])]
            return IRNode('Program', body=body)

        elif node_type == 'FunctionDeclaration':
            name = node['id']['name'] if node.get('id') else None
            params = [param['name'] for param in node.get('params', [])]
            body = self._process_node(node['body'])
            return IRNode('FunctionDeclaration', name=name, params=params, body=body)

        elif node_type == 'VariableDeclaration':
            declarations = [self._process_node(d) for d in node.get('declarations', [])]
            kind = node.get('kind')
            return IRNode('VariableDeclaration', declarations=declarations, kind=kind)

        elif node_type == 'VariableDeclarator':
            id = self._process_node(node['id'])
            init = self._process_node(node['init']) if node.get('init') else None
            return IRNode('VariableDeclarator', id=id, init=init)

        elif node_type == 'CallExpression':
            callee = self._process_node(node['callee'])
            arguments = [self._process_node(arg) for arg in node.get('arguments', [])]
            return IRNode('CallExpression', callee=callee, arguments=arguments)

        elif node_type == 'Identifier':
            name = node.get('name')
            return IRNode('Identifier', name=name)

        elif node_type == 'Literal':
            value = node.get('value')
            return IRNode('Literal', value=value)

        # 处理更多的节点类型...

        else:
            # 对于未处理的节点类型，记录类型名称
            return IRNode('Unhandled', node_type=node_type)
