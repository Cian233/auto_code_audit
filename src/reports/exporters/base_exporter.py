# reports/exporters/base_exporter.py

from abc import ABC, abstractmethod

class BaseExporter(ABC):
    def __init__(self, results):
        self.results = results

    @abstractmethod
    def export(self, output_dir):
        pass
