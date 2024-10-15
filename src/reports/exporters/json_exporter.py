# reports/exporters/json_exporter.py

import os
import json
from .base_exporter import BaseExporter

class JSONExporter(BaseExporter):
    def __init__(self, results):
        super().__init__(results)

    def export(self, output_dir):
        output_path = os.path.join(output_dir, 'audit_report.json')
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(self.results, json_file, ensure_ascii=False, indent=4)
        return output_path
