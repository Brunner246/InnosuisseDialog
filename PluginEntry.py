# generated requirements.txt with pipreqs .\

import sys
import utility_controller as uc
from PyQt5.QtWidgets import QWidget

PLUGIN_PATH = uc.get_plugin_path()

sys.path.append(PLUGIN_PATH)
from View.ParentDialog import ParentDialog
from Controller.SimpleTextController import SimpleTextController
from Controller.ComplexTextController import ComplexTextController
from Model.Page1Model import Page1Model
from Model.Page2Model import Page2Model
from Model.BaseModel import BaseModel

# DEBUG TOGGLE
DEBUG = False

if DEBUG:
    sys.path.append(r'D:\Python\PycharmProjects\InnosuisseDialogEnv\Lib\site-packages')
    import pydevd_pycharm
    pydevd_pycharm.settrace('localhost', port=3003, stdoutToServer=True, stderrToServer=True)

if __name__ == "__main__":
    window_handle = uc.get_3d_hwnd()
    parent_widget = QWidget.find(window_handle)

    simple_controller = SimpleTextController()
    complex_controller = ComplexTextController()

    base_model = BaseModel()
    base_model.model1 = Page1Model(complex_controller)
    base_model.model2 = Page2Model(simple_controller)

    parent_dialog = ParentDialog(base_model, parent_widget)
    parent_dialog.show()
