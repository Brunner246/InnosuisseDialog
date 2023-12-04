import sys
import utility_controller as uc

PLUGIN_PATH = uc.get_plugin_path()

sys.path.append(PLUGIN_PATH)
from ParentDialog import ParentDialog

if __name__ == "__main__":
    parent_dialog = ParentDialog()
    parent_dialog.show()
