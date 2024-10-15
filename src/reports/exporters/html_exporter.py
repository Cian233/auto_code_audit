# reports/exporters/html_exporter.py

import os
from jinja2 import Environment, FileSystemLoader
from .base_exporter import BaseExporter

class HTMLExporter(BaseExporter):
    def __init__(self, results, templates_dir):
        super().__init__(results)
        self.templates_dir = templates_dir

    def export(self, output_dir):
        env = Environment(loader=FileSystemLoader(self.templates_dir))
        template = env.get_template('report_template.html')

        report_content = template.render(vulnerabilities=self.results)

        output_path = os.path.join(output_dir, 'audit_report.html')
        with open(output_path, 'w', encoding='utf-8') as report_file:
            report_file.write(report_content)

        return output_path
