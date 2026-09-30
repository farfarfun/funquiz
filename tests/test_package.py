import funquiz
from importlib.metadata import version


def test_version():
    assert funquiz.__version__ == version("funquiz")


def test_typed_marker_is_packaged():
    from importlib.resources import files

    assert files("funquiz").joinpath("py.typed").is_file()
