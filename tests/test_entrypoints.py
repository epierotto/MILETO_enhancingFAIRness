import importlib


def test_src_entrypoint_modules_are_importable():
    importlib.import_module("src.app")
    importlib.import_module("src.cli")
    importlib.import_module("src.gui_app")
