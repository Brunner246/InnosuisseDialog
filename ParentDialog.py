# COMPILE UI FILE TO PY FILE
# pyuic5 -o main_window_ui.py ui/main_window.ui

from PyQt5.QtWidgets import QDialog

import sys
import utility_controller as uc

PLUGIN_PATH = uc.get_plugin_path()
sys.path.append(PLUGIN_PATH)

from ParentDialog_ui import Ui_Dialog
from ChildPage1 import ChildPage1


class ParentDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__add_tab_widgets()

    def __add_tab_widgets(self):
        self.tabWidget.addTab(ChildPage1(), "Child Page 1")
