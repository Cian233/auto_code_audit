# utils/decorators.py

import time
from functools import wraps
from .logger import get_logger

logger = get_logger(__name__)

def log_execution(func):
    """
    记录函数执行的装饰器。
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"开始执行函数: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"函数执行完成: {func.__name__}")
        return result
    return wrapper

def time_execution(func):
    """
    测量函数执行时间的装饰器。
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.debug(f"开始计时函数: {func.__name__}")
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.debug(f"函数计时结束: {func.__name__}")
        logger.info(f"函数 {func.__name__} 执行时间: {end_time - start_time:.4f} 秒")
        return result
    return wrapper
