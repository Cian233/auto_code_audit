# src/__init__.py

# 导入常用的模块，方便外部使用
from .parsers import ParserFactory
from .normalizers import *
from .analyzers import *
from .machine_learning import *
from .reports import ReportGenerator
from .extensions import PluginManager
from .interfaces import CLIInterface, WebInterface, APIInterface
from .utils import Logger, ConfigLoader

# 初始化全局的配置和日志
config = ConfigLoader.load_config()
logger = Logger.get_logger(config['log_level'])
