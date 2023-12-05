import sys

import element_controller as ec
import utility_controller as uc

PLUGIN_PATH = uc.get_plugin_path()
sys.path.append(PLUGIN_PATH)
from Utils.TextPositionData import TextPositionData


class SimpleTextController:
    def __init__(self):
        pass

    def test_function(self):
        print(uc.get_3d_file_path())

    def create_text_object(self, text: str, position: TextPositionData, size: float) -> int:
        return ec.create_text_object(text, position.position, position.xl, position.zl, size)



