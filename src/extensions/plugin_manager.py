# src/extensions/plugin_manager.py

import os
import importlib.util
from abc import ABC, abstractmethod
from typing import List, Type

class PluginInterface(ABC):
    """
    插件接口，所有插件必须继承并实现此接口。
    """

    @abstractmethod
    def activate(self):
        """
        激活插件时调用的方法。
        """
        pass

    @abstractmethod
    def deactivate(self):
        """
        停用插件时调用的方法。
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """
        返回插件的名称。
        """
        pass

class PluginManager:
    """
    插件管理器，负责加载和管理插件。
    """

    def __init__(self, plugins_directory: str):
        self.plugins_directory = plugins_directory
        self.plugins: List[PluginInterface] = []

    def discover_plugins(self):
        """
        发现插件目录下的所有插件。
        """
        if not os.path.isdir(self.plugins_directory):
            print(f"插件目录 {self.plugins_directory} 不存在。")
            return

        for item in os.listdir(self.plugins_directory):
            item_path = os.path.join(self.plugins_directory, item)
            if os.path.isdir(item_path):
                plugin_main = os.path.join(item_path, 'plugin.py')
                if os.path.isfile(plugin_main):
                    plugin = self.load_plugin(plugin_main)
                    if plugin:
                        self.plugins.append(plugin)

    def load_plugin(self, plugin_path: str) -> PluginInterface:
        """
        加载单个插件。
        """
        module_name = os.path.splitext(os.path.basename(plugin_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, plugin_path)
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # 假设插件模块中有一个名为 Plugin 的类
            if hasattr(module, 'Plugin'):
                plugin_class: Type[PluginInterface] = getattr(module, 'Plugin')
                if issubclass(plugin_class, PluginInterface):
                    plugin_instance = plugin_class()
                    print(f"加载插件: {plugin_instance.get_name()}")
                    return plugin_instance
        print(f"无法加载插件: {plugin_path}")
        return None

    def activate_all_plugins(self):
        """
        激活所有已加载的插件。
        """
        for plugin in self.plugins:
            plugin.activate()

    def deactivate_all_plugins(self):
        """
        停用所有已加载的插件。
        """
        for plugin in self.plugins:
            plugin.deactivate()

    def get_plugins(self) -> List[PluginInterface]:
        """
        获取所有已加载的插件。
        """
        return self.plugins
