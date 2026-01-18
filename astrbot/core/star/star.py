from __future__ import annotations

from dataclasses import dataclass, field
from types import ModuleType
from typing import TYPE_CHECKING, Any

from astrbot.core.config import AstrBotConfig

star_registry: list[StarMetadata] = []
star_map: dict[str, StarMetadata] = {}
"""key 是模块路径，__module__"""

if TYPE_CHECKING:
    from . import Star


@dataclass
class StarMetadata:
    """插件的元数据。

    当 activated 为 False 时，star_cls 可能为 None，请不要在插件未激活时调用 star_cls 的方法。
    """

    name: str | None = None
    """插件名"""
    author: str | None = None
    """插件作者"""
    desc: str | None = None
    """插件简介"""
    version: str | None = None
    """插件版本"""
    repo: str | None = None
    """插件仓库地址"""

    star_cls_type: type[Star] | None = None
    """插件的类对象的类型"""
    module_path: str | None = None
    """插件的模块路径"""

    star_cls: Star | None = None
    """插件的类对象"""
    module: ModuleType | None = None
    """插件的模块对象"""
    root_dir_name: str | None = None
    """插件的目录名称"""
    reserved: bool = False
    """是否是 AstrBot 的保留插件"""

    activated: bool = True
    """是否被激活"""

    config: AstrBotConfig | None = None
    """插件配置"""

    star_handler_full_names: list[str] = field(default_factory=list)
    """注册的 Handler 的全名列表"""

    display_name: str | None = None
    """用于展示的插件名称"""

    logo_path: str | None = None
    """插件 Logo 的路径"""

    frontend_entry: str | None = None
    """插件前端入口（ESM 模块 URL 或相对插件目录的文件路径）"""

    frontend_meta: dict[str, Any] | None = None
    """插件前端路由 meta（会透传给前端 router 的 meta 字段）"""

    def __str__(self) -> str:
        return f"Plugin {self.name} ({self.version}) by {self.author}: {self.desc}"

    def __repr__(self) -> str:
        return f"Plugin {self.name} ({self.version}) by {self.author}: {self.desc}"
