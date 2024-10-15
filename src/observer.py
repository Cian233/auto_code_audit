# src/observer.py

from abc import ABC, abstractmethod

class VulnerabilityEvent:
    """
    定义漏洞事件，包含漏洞类型、位置和详细信息
    """
    def __init__(self, vuln_type, location, details):
        self.vuln_type = vuln_type
        self.location = location
        self.details = details

class Observer(ABC):
    """
    抽象观察者接口，定义更新方法
    """
    @abstractmethod
    def update(self, event):
        pass

class Subject(ABC):
    """
    抽象主题接口，定义注册、注销观察者和通知方法
    """
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister_observer(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify_observers(self, event):
        for observer in self._observers:
            observer.update(event)

class AnalyzerContext(Subject):
    """
    分析器上下文，继承自Subject，管理分析策略和漏洞事件
    """
    def __init__(self):
        super().__init__()
        self._strategies = []

    def add_strategy(self, strategy):
        self._strategies.append(strategy)

    def run_analysis(self, ir):
        for strategy in self._strategies:
            findings = strategy.analyze(ir)
            for finding in findings:
                event = VulnerabilityEvent(finding.vuln_type, finding.location, finding.details)
                self.notify_observers(event)

class VulnerabilityObserver(Observer):
    """
    漏洞观察者，实现Observer接口，收集漏洞信息
    """
    def __init__(self):
        self.findings = []

    def update(self, event):
        self.findings.append(event)

    def update_from_ml(self, ml_findings):
        """
        从机器学习模型获取的漏洞信息进行更新
        """
        for finding in ml_findings:
            event = VulnerabilityEvent(finding['vuln_type'], finding['location'], finding['details'])
            self.findings.append(event)
