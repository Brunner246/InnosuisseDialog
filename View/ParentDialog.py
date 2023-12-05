# COMPILE UI FILE TO PY FILE
# pyuic5 -o main_window_ui.py ui/main_window.ui

from PyQt5.QtWidgets import QDialog

import sys
import utility_controller as uc

PLUGIN_PATH = uc.get_plugin_path()
sys.path.append(PLUGIN_PATH)

from View.ParentDialog_ui import Ui_Dialog
from View.ChildPage1 import ChildPage1
from View.ChildPage2 import ChildPage2
from Model.Page1Model import Page1Model
from Model.Page2Model import Page2Model


class ParentDialog(QDialog, Ui_Dialog):
    def __init__(self, model1: Page1Model, model2: Page2Model, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__model1 = model1
        self.__model2 = model2
        self.__page_1 = ChildPage1(self.__model1)
        self.__page_2 = ChildPage2(self.__model2)
        self.__add_tab_widgets()

    def __add_tab_widgets(self):
        self.tabWidget.addTab(self.__page_1, "Complex Text Object")
        self.tabWidget.addTab(self.__page_2, "Simple Text Object")