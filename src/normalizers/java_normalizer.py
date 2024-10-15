# src/normalizers/java_normalizer.py

import javalang
from .base_normalizer import BaseNormalizer
from .ir import IRNode

class JavaNormalizer(BaseNormalizer):
    """
    JavaNormalizer 用于将 Java 的 AST 转换为统一的中间表示。
    """

    def normalize(self, java_ast: javalang.ast.Node) -> IRNode:
        """
        实现对 Java AST 的规范化处理。
        :param java_ast: Java AST 对象
        :return: 统一的中间表示（IR）
        """
        ir = self._process_node(java_ast)
        return ir

    def _process_node(self, node) -> IRNode:
        """
        递归处理 AST 节点，转换为统一的 IR 节点。
        :param node: AST 节点
        :return: IR 节点
        """
        node_type = type(node).__name__

        # 处理不同类型的节点
        if isinstance(node, javalang.tree.CompilationUnit):
            types = [self._process_node(t) for t in node.types]
            return IRNode('CompilationUnit', types=types)

        elif isinstance(node, javalang.tree.ClassDeclaration):
            name = node.name
            methods = [self._process_node(m) for m in node.methods]
            fields = [self._process_node(f) for f in node.fields]
            return IRNode('ClassDeclaration', name=name, methods=methods, fields=fields)

        elif isinstance(node, javalang.tree.MethodDeclaration):
            name = node.name
            parameters = [param.name for param in node.parameters]
            body = self._process_node(node.body) if node.body else None
            return IRNode('MethodDeclaration', name=name, parameters=parameters, body=body)

        elif isinstance(node, javalang.tree.BlockStatement):
            statements = [self._process_node(s) for s in node.statements]
            return IRNode('BlockStatement', statements=statements)

        elif isinstance(node, javalang.tree.StatementExpression):
            expression = self._process_node(node.expression)
            return IRNode('StatementExpression', expression=expression)

        elif isinstance(node, javalang.tree.MethodInvocation):
            qualifier = node.qualifier
            member = node.member
            arguments = [self._process_node(arg) for arg in node.arguments]
            return IRNode('MethodInvocation', qualifier=qualifier, member=member, arguments=arguments)

        elif isinstance(node, javalang.tree.Literal):
            return IRNode('Literal', value=node.value)

        elif isinstance(node, javalang.tree.BinaryOperation):
            operator = node.operator
            left = self._process_node(node.operandl)
            right = self._process_node(node.operandr)
            return IRNode('BinaryOperation', operator=operator, left=left, right=right)

        # 处理更多的节点类型...

        else:
            # 对于未处理的节点类型，记录类型名称
            return IRNode('Unhandled', node_type=node_type)
