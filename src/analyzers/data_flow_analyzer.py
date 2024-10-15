# analyzers/data_flow_analyzer.py

from .analyzer_strategy import AnalyzerStrategy
from .events import VulnerabilityEvent
from ..utils.logger import logger

class DataFlowAnalyzer(AnalyzerStrategy):
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        """
        注册观察者，用于接收漏洞发现事件。

        :param observer: 观察者对象，需实现update方法
        """
        self.observers.append(observer)

    def notify_observers(self, event):
        """
        通知所有注册的观察者。

        :param event: 漏洞事件对象
        """
        for observer in self.observers:
            observer.update(event)

    def analyze(self, ir, context):
        """
        对中间表示进行数据流分析。

        :param ir: 中间表示（AST或IR）
        :param context: 上下文信息
        :return: 分析结果
        """
        logger.info("Starting data flow analysis.")
        # 示例：遍历IR，进行简单的数据流分析
        for node in ir.nodes():
            if self.is_potential_vulnerability(node):
                event = VulnerabilityEvent(
                    vuln_type="Data Flow Issue",
                    location=node.location,
                    details="Potential data flow vulnerability detected."
                )
                self.notify_observers(event)
                logger.debug(f"Vulnerability detected at {node.location}")
        logger.info("Data flow analysis completed.")

    def is_potential_vulnerability(self, node):
        """
        判断节点是否存在潜在的漏洞。

        :param node: IR中的节点
        :return: 布尔值，表示是否存在漏洞
        """
        # 这里实现具体的数据流分析算法
        # 示例：检查变量的未初始化使用
        if node.type == "VariableUsage" and not node.is_initialized:
            return True
        return False
