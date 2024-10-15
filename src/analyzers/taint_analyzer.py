# analyzers/taint_analyzer.py

from .analyzer_strategy import AnalyzerStrategy
from .events import VulnerabilityEvent
from ..utils.logger import logger

class TaintAnalyzer(AnalyzerStrategy):
    def __init__(self):
        self.observers = []
        # 定义污点源和污点汇
        self.taint_sources = set()
        self.taint_sinks = set()
        self.taint_flows = {}

    def register_observer(self, observer):
        """
        注册观察者。

        :param observer: 观察者对象
        """
        self.observers.append(observer)

    def notify_observers(self, event):
        """
        通知所有观察者。

        :param event: 漏洞事件对象
        """
        for observer in self.observers:
            observer.update(event)

    def analyze(self, ir, context):
        """
        进行污点分析。

        :param ir: 中间表示
        :param context: 上下文信息
        :return: 分析结果
        """
        logger.info("Starting taint analysis.")
        self.initialize_taint_sources_and_sinks(context)
        self.perform_taint_analysis(ir)
        logger.info("Taint analysis completed.")

    def initialize_taint_sources_and_sinks(self, context):
        """
        初始化污点源和污点汇。

        :param context: 上下文信息
        """
        # 从配置或规则中加载污点源和污点汇
        self.taint_sources = context.get('taint_sources', set())
        self.taint_sinks = context.get('taint_sinks', set())

    def perform_taint_analysis(self, ir):
        """
        执行污点分析算法。

        :param ir: 中间表示
        """
        # 实现污点传播逻辑
        for node in ir.nodes():
            if self.is_taint_source(node):
                self.propagate_taint(node)
            elif self.is_taint_sink(node):
                if self.is_tainted(node):
                    event = VulnerabilityEvent(
                        vuln_type="Taint Flow Detected",
                        location=node.location,
                        details="Untrusted data flows into a sensitive sink."
                    )
                    self.notify_observers(event)
                    logger.debug(f"Taint flow detected at {node.location}")

    def is_taint_source(self, node):
        """
        判断节点是否为污点源。

        :param node: IR节点
        :return: 布尔值
        """
        return node.type == "Input" and node.name in self.taint_sources

    def is_taint_sink(self, node):
        """
        判断节点是否为污点汇。

        :param node: IR节点
        :return: 布尔值
        """
        return node.type == "FunctionCall" and node.name in self.taint_sinks

    def is_tainted(self, node):
        """
        判断节点是否被污点污染。

        :param node: IR节点
        :return: 布尔值
        """
        # 检查节点是否在污点流中
        return node in self.taint_flows

    def propagate_taint(self, node):
        """
        从污点源开始，传播污点。

        :param node: 污点源节点
        """
        # 实现污点传播算法
        # 示例：使用深度优先搜索传播污点
        stack = [node]
        while stack:
            current_node = stack.pop()
            self.taint_flows[current_node] = True
            for child in current_node.children:
                if child not in self.taint_flows:
                    stack.append(child)
