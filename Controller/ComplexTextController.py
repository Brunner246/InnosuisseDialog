import sys

import element_controller as ec
import cadwork
import utility_controller as uc

PLUGIN_PATH = uc.get_plugin_path()
sys.path.append(PLUGIN_PATH)
from Utils.TextPositionData import TextPositionData


class ComplexTextController:
    def __init__(self):
        pass

    def test_function(self):
        print(uc.get_3d_file_path())

    def create_text_object_with_options(self, position: TextPositionData,
                                        options: cadwork.text_object_options) -> int:
        return ec.create_text_object_with_options(position.position, position.xl, position.zl, options)
