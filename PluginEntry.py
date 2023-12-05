# generated requirements.txt with pipreqs .\

import sys
import utility_controller as uc


PLUGIN_PATH = uc.get_plugin_path()

sys.path.append(PLUGIN_PATH)
from ParentDialog import ParentDialog
from CwAPIController import CwAPIController
from Page1Model import Page1Model
from Page2Model import Page2Model

if __name__ == "__main__":
    controller = CwAPIController()
    model1 = Page1Model(controller)
    model2 = Page2Model(controller)
    parent_dialog = ParentDialog(model1, model2)
    parent_dialog.show()
