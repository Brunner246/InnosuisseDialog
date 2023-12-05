import sys
import time
from typing import List

import element_controller as ec
import utility_controller as uc
from PyQt5.QtCore import QObject, pyqtSignal

PLUGIN_PATH = uc.get_plugin_path()

sys.path.append(PLUGIN_PATH)

from Controller.SimpleTextController import SimpleTextController
from Utils.TextPositionData import create_text_position_data


class Page2Model(QObject):
    timer_signal = pyqtSignal(float)
    TEXT_FONT_SIZE: float = 100.0

    def __init__(self, controller: SimpleTextController, parent=None):
        super().__init__(parent)
        self.__controller = controller
        self.__elapsed_time: float = 0

    def create_text_object(self, text: str, count: int) -> List[int]:
        start = time.time()
        uc.disable_auto_display_refresh()
        position_data = create_text_position_data()
        element_ids = [self.__controller.create_text_object(text,
                                                            position_data,
                                                            Page2Model.TEXT_FONT_SIZE) for _ in range(0, count)]
        uc.enable_auto_display_refresh()
        ec.recreate_elements(element_ids)
        end = time.time()
        self.__elapsed_time = end - start
        self.timer_signal.emit(self.__elapsed_time)
        return element_ids
