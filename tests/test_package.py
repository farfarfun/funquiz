import importlib
from importlib.metadata import PackageNotFoundError, version

import funquiz


def test_version():
    assert funquiz.__version__ == version("funquiz")


def test_typed_marker_is_packaged():
    from importlib.resources import files

    assert files("funquiz").joinpath("py.typed").is_file()


def test_version_fallback_when_distribution_missing(monkeypatch):
    """包未安装（如直接从源码运行）时，`__version__` 应回退为 "0.0.0"。"""

    def _raise_not_found(name: str) -> str:
        raise PackageNotFoundError(name)

    monkeypatch.setattr("importlib.metadata.version", _raise_not_found)
    try:
        importlib.reload(funquiz)
        assert funquiz.__version__ == "0.0.0"
    finally:
        importlib.reload(funquiz)
