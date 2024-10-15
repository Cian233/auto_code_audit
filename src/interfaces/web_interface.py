# interfaces/web_interface.py

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from src.parsers.parser_factory import ParserFactory
from src.analyzers.analyzer_strategy import AnalyzerStrategy
from src.reports.report_generator import ReportGenerator
from src.utils.config_loader import ConfigLoader

app = Flask(__name__)

# 设置上传文件的保存路径和允许的文件类型
UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = {'py', 'java', 'js', 'cpp'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class WebInterface:
    def __init__(self):
        self.app = app
        self._setup_routes()
    
    def _setup_routes(self):
        self.app.add_url_rule('/', 'index', self.index, methods=['GET', 'POST'])
        self.app.add_url_rule('/report/<filename>', 'report', self.report)

    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    def index(self):
        if request.method == 'POST':
            # 检查是否有文件上传
            if 'file' not in request.files:
                return 'No file part', 400
            file = request.files['file']
            if file.filename == '':
                return 'No selected file', 400
            if file and self.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                
                # 获取语言类型
                language = request.form.get('language')
                
                # Step 1: Parse the source code
                parser = ParserFactory.get_parser(language)
                ast = parser.parse(file_path)
                
                # Step 2: Analyze the code
                analyzer = AnalyzerStrategy()
                analyzer_result = analyzer.analyze(ast)
                
                # Step 3: Generate report
                report_generator = ReportGenerator()
                report = report_generator.generate(analyzer_result, format='html')
                
                # Step 4: Save report
                report_filename = f"{filename}_report.html"
                report_path = os.path.join(app.config['UPLOAD_FOLDER'], report_filename)
                with open(report_path, 'w', encoding='utf-8') as f:
                    f.write(report)
                
                return redirect(url_for('report', filename=report_filename))
        return render_template('index.html')
    
    def report(self, filename):
        return render_template(filename)
    
    def run(self, host='0.0.0.0', port=5000):
        self.app.run(host=host, port=port)

if __name__ == '__main__':
    web_interface = WebInterface()
    web_interface.run()
