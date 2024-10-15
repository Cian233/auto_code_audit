# src/normalizers/ir.py

from typing import Any, Dict, List, Union

class IRNode:
    """
    IRNode 定义了统一的中间表示节点。
    """

    def __init__(self, node_type: str, **kwargs):
        self.type = node_type
        self.attributes = kwargs

    def to_dict(self) -> Dict[str, Any]:
        """
        将 IR 节点转换为字典表示，方便序列化和处理。
        """
        result = {'type': self.type}
        for key, value in self.attributes.items():
            if isinstance(value, IRNode):
                result[key] = value.to_dict()
            elif isinstance(value, list):
                result[key] = [
                    item.to_dict() if isinstance(item, IRNode) else item
                    for item in value
                ]
            else:
                result[key] = value
        return result

    def __repr__(self):
        return f"IRNode(type='{self.type}', attributes={self.attributes})"
