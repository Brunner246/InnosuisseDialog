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

if __name__ == "__main__":
    window_handle = uc.get_3d_hwnd()
    parent_widget = QWidget.find(window_handle)
    simple_controller = SimpleTextController()
    complex_controller = ComplexTextController()
    model1 = Page1Model(complex_controller)
    model2 = Page2Model(simple_controller)
    parent_dialog = ParentDialog(model1, model2, parent_widget)
    parent_dialog.show()
