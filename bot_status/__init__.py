from src.plugin_system.base.plugin_metadata import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="BotStatus",
    description="一个用于生成机器人和系统状态图的插件。",
    usage="/status",
    version="1.0.0",
    author="YiShan",
    license="GPL-v3.0-or-later",
    repository_url="https://github.com/minecraft1024a",
    keywords=["status", "statistics", "management"],
    extra={
        "plugin_type": "info",
    },
    python_dependencies=["psutil", "Pillow"]
)
