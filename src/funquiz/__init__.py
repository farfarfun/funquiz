"""funquiz 包元数据。"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__: str = version("funquiz")
except PackageNotFoundError:
    __version__ = "0.0.0"
