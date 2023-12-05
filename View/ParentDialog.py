# COMPILE UI FILE TO PY FILE
# pyuic5 -o main_window_ui.py ui/main_window.ui

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt

import sys
import utility_controller as uc


PLUGIN_PATH = uc.get_plugin_path()
sys.path.append(PLUGIN_PATH)

from View.ParentDialog_ui import Ui_Dialog
from View.ChildPage1 import ChildPage1
from View.ChildPage2 import ChildPage2
from Model.BaseModel import BaseModel


class ParentDialog(QDialog, Ui_Dialog):
    def __init__(self, model: BaseModel, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_window_flags()
        self.__model = model
        self.__page_1 = ChildPage1(self.__model.model1, self)
        self.__page_2 = ChildPage2(self.__model.model2, self)
        self.__add_tab_widgets()
        self.setAttribute(Qt.WA_DeleteOnClose)

    def __add_tab_widgets(self):
        self.tabWidget.addTab(self.__page_1, "Complex Text Object")
        self.tabWidget.addTab(self.__page_2, "Simple Text Object")

    def set_window_flags(self):
        flags = Qt.Dialog
        flags |= Qt.WindowTitleHint
        flags |= Qt.WindowSystemMenuHint
        flags |= Qt.MSWindowsFixedSizeDialogHint
        flags |= Qt.WindowCloseButtonHint
        self.setWindowFlags(flags)
