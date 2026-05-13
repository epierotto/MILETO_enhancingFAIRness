import logging
import os
import sys

from src.cli import main_cli
from src.gui_app import main_gui


logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler("logs"), logging.StreamHandler()],
)


def _configure_frozen_paths() -> None:
    if getattr(sys, "frozen", False):
        bundle_dir = sys._MEIPASS
        os.environ["PATH"] = (
            os.path.join(bundle_dir, "graphviz")
            + os.pathsep
            + os.path.join(bundle_dir, "wkhtmltopdf")
            + os.pathsep
            + os.environ["PATH"]
        )


def main() -> None:
    _configure_frozen_paths()
    try:
        if len(sys.argv) > 1:
            main_cli()
        else:
            main_gui()
    except Exception as exc:
        logging.error(f"An error occurred: {exc}", exc_info=True)


if __name__ == "__main__":
    main()
