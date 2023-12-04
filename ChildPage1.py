#  python -m PyQt5.uic.pyuic -x ./ChildPage1.ui -o ChildPage1.py
# python -m PyQt5.uic.pyuic -x ./ChildPage1.ui -o ChildPage1_ui.py

from PyQt5.QtWidgets import QWidget, QPushButton

import sys
import utility_controller as uc

PLUGIN_PATH = uc.get_plugin_path()
sys.path.append(PLUGIN_PATH)

from ChildPage1_ui import Ui_Form


class ChildPage1(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button = QPushButton("Click me")
