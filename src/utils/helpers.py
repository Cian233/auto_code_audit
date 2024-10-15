# utils/helpers.py

from functools import wraps
from .logger import get_logger
import os

logger = get_logger(__name__)

def Singleton(cls):
    """
    单例模式的装饰器。
    """
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            logger.debug(f"创建单例实例: {cls.__name__}")
            instances[cls] = cls(*args, **kwargs)
        else:
            logger.debug(f"使用已有的单例实例: {cls.__name__}")
        return instances[cls]

    return get_instance

def cache_result(func):
    """
    简单的结果缓存装饰器。
    """
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in cache:
            logger.debug(f"缓存函数结果: {func.__name__}，参数: {key}")
            cache[key] = func(*args, **kwargs)
        else:
            logger.debug(f"使用缓存的函数结果: {func.__name__}，参数: {key}")
        return cache[key]
    return wrapper

def get_file_extensions(language):
    extensions = {
        'Python': ['.py'],
        'Java': ['.java'],
        'JavaScript': ['.js'],
        # 添加其他语言的扩展名
    }
    return extensions.get(language, [])

def detect_language(filename):
    extension = os.path.splitext(filename)[1].lower()
    extension_map = {
        '.py': 'Python',
        '.java': 'Java',
        '.js': 'JavaScript',
        # 添加其他扩展名的映射
    }
    return extension_map.get(extension, 'Unknown')