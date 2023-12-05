import sys
import time
from typing import List

import cadwork
import element_controller as ec
import utility_controller as uc
from PyQt5.QtCore import QObject, pyqtSignal

PLUGIN_PATH = uc.get_plugin_path()

sys.path.append(PLUGIN_PATH)

from Controller.ComplexTextController import ComplexTextController
from Utils.TextPositionData import create_text_position_data, create_text_option_data


class Page1Model(QObject):
    timer_signal = pyqtSignal(float)

    def __init__(self, controller: ComplexTextController, parent=None):
        super().__init__(parent)
        self.__controller = controller
        self.__elapsed_time: float = 0

    def test_function(self):
        self.__controller.test_function()

    def create_text_object_options(self, text: str, count: int, element_type: cadwork.text_object_options) -> List[int]:
        start = time.time()
        uc.disable_auto_display_refresh()
        text_position_data = create_text_position_data()
        text_options = create_text_option_data(text, element_type)
        element_ids = [self.__controller.create_text_object_with_options
                       (text_position_data, text_options) for _ in range(0, count)]
        uc.enable_auto_display_refresh()
        ec.recreate_elements(element_ids)
        end = time.time()
        self.__elapsed_time = end - start
        self.timer_signal.emit(self.__elapsed_time)
        return element_ids

