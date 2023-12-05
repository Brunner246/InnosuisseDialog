#  python -m PyQt5.uic.pyuic -x ./ChildPage1.ui -o ChildPage1.py
# python -m PyQt5.uic.pyuic -x ./ChildPage1.ui -o ChildPage1_ui.py

from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox

import sys
import cadwork
import utility_controller as uc

PLUGIN_PATH = uc.get_plugin_path()
sys.path.append(PLUGIN_PATH)

from ChildPage1_ui import Ui_Form
from Page1Model import Page1Model
from Messagebox import show_info_box


class ChildPage1(QWidget, Ui_Form):
    def __init__(self, model: Page1Model, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__model = model
        self.__text_element_type: cadwork.text_element_type = cadwork.text_element_type.line

        self.cbx_geometry_type.addItems(["line", "surface", "volume"])
        self.pbn_path.clicked.connect(self.__model.test_function)
        self.pbn_text_object.clicked.connect(self.create_text_object_options)
        self.__model.timer_signal.connect(self.__show_info)
        self.cbx_geometry_type.currentIndexChanged.connect(self.__text_geometry_type)

    def create_text_object_options(self):
        self.__model.create_text_object_options(self.led_text.text(), self.spb_count.value(), self.text_element_type)

    def __text_geometry_type(self, index: int):
        if index == 0:
            self.text_element_type = cadwork.text_element_type.line
        elif index == 1:
            self.text_element_type = cadwork.text_element_type.surface
        else:
            self.text_element_type = cadwork.text_element_type.volume

    @property
    def text_element_type(self):
        return self.__text_element_type

    @text_element_type.setter
    def text_element_type(self, value):
        self.__text_element_type = value

    def __show_info(self, seconds: float):
        show_info_box(self, seconds)
