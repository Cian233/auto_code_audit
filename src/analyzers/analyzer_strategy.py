# analyzers/analyzer_strategy.py
from typing import List
from .events import VulnerabilityEvent,Observer

from abc import ABC, abstractmethod

class AnalyzerStrategy(ABC):
    @abstractmethod
    def analyze(self, ir, context):
        """
        对中间表示（IR）进行分析。

        :param ir: 中间表示（抽象语法树或其他形式）
        :param context: 上下文信息，包含配置和辅助数据
        :return: 分析结果，可以是漏洞列表、警告等
        """
        pass

class AnalyzerContext:
    """
    分析器上下文，负责管理分析策略和观察者，并运行分析流程。
    
    使用策略模式来添加和执行不同的分析策略，
    使用观察者模式来通知发现的漏洞。
    """

    def __init__(self):
        """
        初始化 AnalyzerContext，设置空的策略列表和观察者列表。
        """
        self._strategies: List[AnalyzerStrategy] = []
        self._observers: List[Observer] = []

    def register_observer(self, observer: Observer):
        """
        注册一个观察者，用于接收漏洞发现的通知。
        
        Args:
            observer (Observer): 需要注册的观察者实例。
        """
        self._observers.append(observer)

    def add_strategy(self, strategy: AnalyzerStrategy):
        """
        添加一个分析策略到上下文中。
        
        Args:
            strategy (AnalyzerStrategy): 要添加的分析策略实例。
        """
        self._strategies.append(strategy)

    def run_analysis(self, ir):
        """
        运行所有添加的分析策略，对中间表示（IR）进行分析，
        并通知观察者发现的漏洞事件。
        
        Args:
            ir: 规范化后的中间表示（Intermediate Representation）。
        """
        for strategy in self._strategies:
            try:
                findings = strategy.analyze(ir)
                for finding in findings:
                    event = VulnerabilityEvent(
                        vuln_type=finding.type,
                        location=finding.location,
                        details=finding.details
                    )
                    self.__notify_observers(event)
            except Exception as e:
                # 记录异常但不中断整个分析流程
                print(f"Error in strategy {strategy.__class__.__name__}: {e}")

    def __notify_observers(self, event: VulnerabilityEvent):
        """
        内部方法，用于通知所有注册的观察者一个漏洞事件。
        
        Args:
            event (VulnerabilityEvent): 需要通知的漏洞事件。
        """
        for observer in self._observers:
            try:
                observer.update(event)
            except Exception as e:
                # 记录异常但不中断通知流程
                print(f"Error notifying observer {observer.__class__.__name__}: {e}")
