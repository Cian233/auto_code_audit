# reports/report_generator.py

import os
from exporters import HTMLExporter, PDFExporter, JSONExporter

class ReportGenerator:
    def __init__(self, results, output_dir='reports', templates_dir='templates'):
        """
        初始化报告生成器。

        :param results: 分析结果，通常是一个列表，包含漏洞信息的字典。
        :param output_dir: 报告输出目录。
        :param templates_dir: 报告模板目录。
        """
        self.results = results
        self.output_dir = output_dir
        self.templates_dir = templates_dir

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_report(self, format='html'):
        """
        生成报告。

        :param format: 报告格式，支持'html'、'pdf'、'json'。
        """
        if format == 'html':
            exporter = HTMLExporter(self.results, self.templates_dir)
        elif format == 'pdf':
            exporter = PDFExporter(self.results, self.templates_dir)
        elif format == 'json':
            exporter = JSONExporter(self.results)
        else:
            raise ValueError(f"Unsupported format: {format}")

        file_path = exporter.export(self.output_dir)
        print(f"Report generated at: {file_path}")
