# utils/config_loader.py

import os
import yaml
from .helpers import Singleton

@Singleton
class ConfigLoader:
    """
    配置文件加载器，使用单例模式。
    """
    def __init__(self, config_file='config.yaml'):
        self._config_file = config_file
        self._config = None
        self._load_config()

    def _load_config(self):
        if os.path.exists(self._config_file):
            with open(self._config_file, 'r') as f:
                self._config = yaml.safe_load(f)
        else:
            raise FileNotFoundError(f"配置文件 {self._config_file} 不存在")

    def get(self, key, default=None):
        keys = key.split('.')
        value = self._config
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default

    def reload(self):
        """
        重新加载配置文件。
        """
        self._load_config()
