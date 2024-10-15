# analyzers/sensitive_function_detector.py

from .analyzer_strategy import AnalyzerStrategy
from .events import VulnerabilityEvent
from ..utils.logger import logger
from ..data.sensitive_functions_loader import SensitiveFunctionsLoader

class SensitiveFunctionDetector(AnalyzerStrategy):
    def __init__(self, language):
        self.observers = []
        self.language = language
        self.sensitive_functions = SensitiveFunctionsLoader.load(language)

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
        分析代码中的敏感函数调用。

        :param ir: 中间表示
        :param context: 上下文信息
        :return: 分析结果
        """
        logger.info("Starting sensitive function detection.")
        for node in ir.nodes():
            if node.type == "FunctionCall":
                function_name = node.name
                if function_name in self.sensitive_functions:
                    event = VulnerabilityEvent(
                        vuln_type="Sensitive Function Call",
                        location=node.location,
                        details=f"Sensitive function '{function_name}' called."
                    )
                    self.notify_observers(event)
                    logger.debug(f"Sensitive function call detected at {node.location}")
        logger.info("Sensitive function detection completed.")
