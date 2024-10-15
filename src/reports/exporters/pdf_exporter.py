# reports/exporters/pdf_exporter.py

import os
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from .base_exporter import BaseExporter

class PDFExporter(BaseExporter):
    def __init__(self, results, templates_dir):
        super().__init__(results)
        self.templates_dir = templates_dir

    def export(self, output_dir):
        env = Environment(loader=FileSystemLoader(self.templates_dir))
        template = env.get_template('report_template.html')  # 可以复用HTML模板

        report_content = template.render(vulnerabilities=self.results)

        html = HTML(string=report_content)

        output_path = os.path.join(output_dir, 'audit_report.pdf')
        html.write_pdf(output_path)

        return output_path
