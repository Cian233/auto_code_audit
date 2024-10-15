# analyzers/events.py

class VulnerabilityEvent:
    def __init__(self, vuln_type, location, details):
        """
        漏洞事件对象，包含漏洞的相关信息。

        :param vuln_type: 漏洞类型
        :param location: 漏洞位置，通常为文件名和行号
        :param details: 漏洞的详细描述
        """
        self.vuln_type = vuln_type
        self.location = location
        self.details = details

class Observer:
    def update(self, event):
        """
        当被观察的对象发生变化时，调用此方法。

        :param event: 漏洞事件对象
        """
        pass

class Subject:
    def __init__(self):
        self.observers = []

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
