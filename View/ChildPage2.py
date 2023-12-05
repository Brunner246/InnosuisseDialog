from PyQt5.QtWidgets import QWidget

import sys
import utility_controller as uc

PLUGIN_PATH = uc.get_plugin_path()
sys.path.append(PLUGIN_PATH)

from Model.Page2Model import Page2Model
from View.ChildPage2_ui import Ui_Form
from Utils.Messagebox import show_info_box


class ChildPage2(QWidget, Ui_Form):
    def __init__(self, model: Page2Model, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.model = model

        self.pbn_create.clicked.connect(self.create_text_object)
        self.model.timer_signal.connect(self.__show_info)

    def create_text_object(self):
        self.model.create_text_object(self.led_text.text(), self.spb_count.value())

    def __show_info(self, seconds: float):
        show_info_box(self, seconds)