# 定义基础目录
$baseDir = "auto_code_audit_framework"

# 定义目录结构
$directories = @(
    "$baseDir",
    "$baseDir\docs",
    "$baseDir\docs\usage.md",
    "$baseDir\docs\development.md",
    "$baseDir\docs\api_reference.md",
    "$baseDir\data",
    "$baseDir\data\sensitive_functions",
    "$baseDir\data\sensitive_functions\python.yml",
    "$baseDir\data\sensitive_functions\java.yml",
    "$baseDir\data\sensitive_functions\javascript.yml",
    "$baseDir\data\rules",
    "$baseDir\data\rules\python_rules.yml",
    "$baseDir\data\rules\java_rules.yml",
    "$baseDir\data\rules\javascript_rules.yml",
    "$baseDir\src",
    "$baseDir\src\__init__.py",
    "$baseDir\src\main.py",
    "$baseDir\src\parsers",
    "$baseDir\src\parsers\__init__.py",
    "$baseDir\src\parsers\parser_factory.py",
    "$baseDir\src\parsers\base_parser.py",
    "$baseDir\src\parsers\python_parser.py",
    "$baseDir\src\parsers\java_parser.py",
    "$baseDir\src\parsers\javascript_parser.py",
    "$baseDir\src\normalizers",
    "$baseDir\src\normalizers\__init__.py",
    "$baseDir\src\normalizers\base_normalizer.py",
    "$baseDir\src\normalizers\python_normalizer.py",
    "$baseDir\src\normalizers\java_normalizer.py",
    "$baseDir\src\analyzers",
    "$baseDir\src\analyzers\__init__.py",
    "$baseDir\src\analyzers\analyzer_strategy.py",
    "$baseDir\src\analyzers\data_flow_analyzer.py",
    "$baseDir\src\analyzers\control_flow_analyzer.py",
    "$baseDir\src\analyzers\sensitive_function_detector.py",
    "$baseDir\src\analyzers\taint_analysis.py",
    "$baseDir\src\analyzers\events.py",
    "$baseDir\src\machine_learning",
    "$baseDir\src\machine_learning\__init__.py",
    "$baseDir\src\machine_learning\model_interface.py",
    "$baseDir\src\machine_learning\codebert_model.py",
    "$baseDir\src\machine_learning\gpt_model.py",
    "$baseDir\src\reports",
    "$baseDir\src\reports\__init__.py",
    "$baseDir\src\reports\report_generator.py",
    "$baseDir\src\reports\templates",
    "$baseDir\src\reports\templates\report_template.html",
    "$baseDir\src\reports\templates\report_template.pdf",
    "$baseDir\src\reports\exporters",
    "$baseDir\src\reports\exporters\html_exporter.py",
    "$baseDir\src\reports\exporters\pdf_exporter.py",
    "$baseDir\src\reports\exporters\json_exporter.py",
    "$baseDir\src\extensions",
    "$baseDir\src\extensions\__init__.py",
    "$baseDir\src\extensions\plugin_manager.py",
    "$baseDir\src\extensions\plugins",
    "$baseDir\src\extensions\plugins\__init__.py",
    "$baseDir\src\interfaces",
    "$baseDir\src\interfaces\__init__.py",
    "$baseDir\src\interfaces\cli_interface.py",
    "$baseDir\src\interfaces\web_interface.py",
    "$baseDir\src\interfaces\api_interface.py",
    "$baseDir\src\utils",
    "$baseDir\src\utils\__init__.py",
    "$baseDir\src\utils\logger.py",
    "$baseDir\src\utils\decorators.py",
    "$baseDir\src\utils\config_loader.py",
    "$baseDir\src\utils\helpers.py",
    "$baseDir\src\observer.py",
    "$baseDir\tests",
    "$baseDir\tests\__init__.py",
    "$baseDir\tests\test_parsers.py",
    "$baseDir\tests\test_normalizers.py",
    "$baseDir\tests\test_analyzers.py",
    "$baseDir\tests\test_machine_learning.py",
    "$baseDir\tests\test_reports.py",
    "$baseDir\tests\test_extensions.py",
    "$baseDir\tests\test_interfaces.py",
    "$baseDir\tests\data",
    "$baseDir\tests\data\sample_code_snippets",
    "$baseDir\tests\data\sample_code_snippets\test_python_code.py",
    "$baseDir\tests\data\sample_code_snippets\test_java_code.java",
    "$baseDir\tests\data\expected_results",
    "$baseDir\tests\data\expected_results\expected_python_results.json",
    "$baseDir\tests\data\expected_results\expected_java_results.json",
    "$baseDir\examples",
    "$baseDir\examples\python",
    "$baseDir\examples\python\example.py",
    "$baseDir\examples\java",
    "$baseDir\examples\java\Example.java",
    "$baseDir\examples\javascript",
    "$baseDir\examples\javascript\example.js",
    "$baseDir\scripts",
    "$baseDir\scripts\install_dependencies.sh",
    "$baseDir\scripts\run_tests.sh",
    "$baseDir\scripts\start_server.sh",
    "$baseDir\LICENSE",
    "$baseDir\.gitignore",
    "$baseDir\README.md",
    "$baseDir\setup.py",
    "$baseDir\requirements.txt"
)

# 创建目录和文件
foreach ($path in $directories) {
    $directory = Split-Path $path
    $file = Split-Path $path -Leaf

    if ($file -and ($file -match "\.")) {
        # 这是一个文件
        $dirPath = $directory
        if (-not (Test-Path -Path $dirPath)) {
            New-Item -ItemType Directory -Path $dirPath -Force | Out-Null
            Write-Output "创建目录: $dirPath"
        }
        if (-not (Test-Path -Path $path)) {
            New-Item -ItemType File -Path $path -Force | Out-Null
            Write-Output "创建文件: $path"
        }
    }
    else {
        # 这是一个目录
        if (-not (Test-Path -Path $path)) {
            New-Item -ItemType Directory -Path $path -Force | Out-Null
            Write-Output "创建目录: $path"
        }
    }
}
