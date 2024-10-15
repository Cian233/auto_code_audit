# src/extensions/plugins/sample_plugin/plugin.py

from extensions.plugin_manager import PluginInterface

class Plugin(PluginInterface):
    def __init__(self):
        self.name = "Sample Plugin"

    def activate(self):
        print(f"{self.get_name()} 已激活。")
        # 插件激活时执行的逻辑
        # 例如，注册新的敏感函数、添加新的分析规则等

    def deactivate(self):
        print(f"{self.get_name()} 已停用。")
        # 插件停用时执行的逻辑
        # 例如，卸载注册的敏感函数、移除分析规则等

    def get_name(self) -> str:
        return self.name
