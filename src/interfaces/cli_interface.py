# interfaces/cli_interface.py

import argparse
from src.parsers.parser_factory import ParserFactory
from src.analyzers.analyzer_strategy import AnalyzerStrategy
from src.reports.report_generator import ReportGenerator
from src.utils.config_loader import ConfigLoader

class CommandLineInterface:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Automatic Code Audit Framework CLI")
        self._setup_arguments()
        
    def _setup_arguments(self):
        self.parser.add_argument('path', help='Path to the source code directory or file.')
        self.parser.add_argument('-l', '--language', help='Programming language of the source code.', required=True)
        self.parser.add_argument('-o', '--output', help='Path to save the audit report.', default='report.html')
        self.parser.add_argument('-f', '--format', help='Report format (html, pdf, json).', default='html')
        self.parser.add_argument('--use-ml', help='Enable machine learning analysis.', action='store_true')
        self.parser.add_argument('--config', help='Path to configuration file.', default=None)

    def run(self):
        args = self.parser.parse_args()
        config = ConfigLoader.load(args.config) if args.config else {}
        
        # Step 1: Parse the source code
        parser = ParserFactory.get_parser(args.language)
        ast = parser.parse(args.path)
        
        # Step 2: Normalize the AST (if needed)
        # Skipping normalization for simplicity
        
        # Step 3: Analyze the code
        analyzer = AnalyzerStrategy()
        analyzer_result = analyzer.analyze(ast)
        
        # Step 4: Optionally use machine learning model
        if args.use_ml:
            from src.machine_learning.model_interface import ModelInterface
            model = ModelInterface.get_model('default')
            ml_results = model.analyze(ast)
            # Merge results
            analyzer_result.merge(ml_results)
        
        # Step 5: Generate report
        report_generator = ReportGenerator()
        report = report_generator.generate(analyzer_result, format=args.format)
        
        # Step 6: Save the report
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"Audit report has been saved to {args.output}")

if __name__ == '__main__':
    cli = CommandLineInterface()
    cli.run()
