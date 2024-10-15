# utils/logger.py

import logging
import logging.config
import os
import yaml

def get_logger(name=None):
    """
    获取日志记录器。
    """
    if not logging.getLogger(name).handlers:
        # 加载日志配置
        config_file = os.path.join(os.path.dirname(__file__), 'logging_config.yaml')
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
        else:
            # 默认配置
            logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)
