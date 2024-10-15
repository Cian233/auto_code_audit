# interfaces/api_interface.py

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
import os
from src.parsers.parser_factory import ParserFactory
from src.analyzers.analyzer_strategy import AnalyzerStrategy
from src.reports.report_generator import ReportGenerator

app = Flask(__name__)
api = Api(app)

# 设置上传文件的保存路径和允许的文件类型
UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = {'py', 'java', 'js', 'cpp'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class CodeAnalysis(Resource):
    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    def post(self):
        if 'file' not in request.files:
            return {'error': 'No file part'}, 400
        file = request.files['file']
        if file.filename == '':
            return {'error': 'No selected file'}, 400
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # 获取语言类型
            language = request.form.get('language')
            if not language:
                return {'error': 'Language is required'}, 400
            
            # Step 1: Parse the source code
            try:
                parser = ParserFactory.get_parser(language)
                ast = parser.parse(file_path)
            except Exception as e:
                return {'error': str(e)}, 500
            
            # Step 2: Analyze the code
            analyzer = AnalyzerStrategy()
            analyzer_result = analyzer.analyze(ast)
            
            # Step 3: Generate report data (in JSON format)
            report_generator = ReportGenerator()
            report_data = report_generator.generate(analyzer_result, format='json')
            
            return jsonify(report_data)
        else:
            return {'error': 'File type not allowed'}, 400

api.add_resource(CodeAnalysis, '/api/analyze')

class APIInterface:
    def run(self, host='0.0.0.0', port=5001):
        app.run(host=host, port=port)

if __name__ == '__main__':
    api_interface = APIInterface()
    api_interface.run()