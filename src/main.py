# src/main.py

import sys
import argparse
import os

from utils import Logger, ConfigLoader
from parsers.parser_factory import ParserFactory
from normalizers import NormalizerFactory
from analyzers.analyzer_strategy import AnalyzerContext
from analyzers.data_flow_analyzer import DataFlowAnalyzer
from analyzers.control_flow_analyzer import ControlFlowAnalyzer
from analyzers.sensitive_function_detector import SensitiveFunctionDetector
from machine_learning.model_interface import MLModelInterface
from reports.report_generator import ReportGenerator
from extensions.plugin_manager import PluginManager
from observer import VulnerabilityObserver

def main():
    # 加载配置
    config = ConfigLoader.load_config()
    logger = Logger.get_logger(config['log_level'])

    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Multi-language Automated Code Audit Framework')
    parser.add_argument('path', help='Path to the source code directory or file')
    parser.add_argument('-l', '--language', help='Programming language of the source code')
    parser.add_argument('-f', '--format', default='html', choices=['html', 'pdf', 'json'],
                        help='Format of the output report')
    parser.add_argument('-o', '--output', help='Output report file name')
    parser.add_argument('--use-ml', action='store_true', help='Use machine learning analysis')
    parser.add_argument('--plugins', nargs='*', help='List of plugins to load')
    args = parser.parse_args()

    source_path = args.path
    language = args.language
    report_format = args.format
    output_file = args.output
    use_ml = args.use_ml
    plugins = args.plugins

    if not os.path.exists(source_path):
        logger.error(f"Source path {source_path} does not exist.")
        sys.exit(1)

    # 如果未指定语言，尝试自动检测
    if not language:
        # TODO: 实现自动检测源代码语言的功能
        logger.error("Programming language is not specified and auto-detection is not implemented yet.")
        sys.exit(1)

    # 加载插件
    plugin_manager = PluginManager()
    if plugins:
        for plugin_name in plugins:
            plugin_manager.load_plugin(plugin_name)

    # 创建解析器并解析源代码
    parser_instance = ParserFactory.get_parser(language)
    ast = parser_instance.parse(source_path)

    # 规范化AST
    normalizer = NormalizerFactory.get_normalizer(language)
    ir = normalizer.normalize(ast)

    # 创建分析器上下文
    analyzer_context = AnalyzerContext()

    # 注册观测者，用于接收漏洞通知
    vulnerability_observer = VulnerabilityObserver()
    analyzer_context.register_observer(vulnerability_observer)

    # 添加分析策略
    data_flow_analyzer = DataFlowAnalyzer()
    control_flow_analyzer = ControlFlowAnalyzer()
    sensitive_function_detector = SensitiveFunctionDetector(language)

    analyzer_context.add_strategy(data_flow_analyzer)
    analyzer_context.add_strategy(control_flow_analyzer)
    analyzer_context.add_strategy(sensitive_function_detector)

    # 运行分析
    analyzer_context.run_analysis(ir)

    # 机器学习模型分析
    if use_ml:
        ml_model = MLModelInterface.get_model(language)
        ml_findings = ml_model.analyze(source_path)
        vulnerability_observer.update_from_ml(ml_findings)

    # 生成报告
    report_generator = ReportGenerator(format=report_format)
    report = report_generator.generate_report(vulnerability_observer.findings)

    # 输出报告
    if output_file:
        report_generator.save_report(report, output_file)
    else:
        default_output = f"audit_report.{report_format}"
        report_generator.save_report(report, default_output)

    logger.info("Code audit completed successfully.")

if __name__ == "__main__":
    main()
