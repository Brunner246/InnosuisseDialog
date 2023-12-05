import sys
from dataclasses import dataclass

import utility_controller as uc

PLUGIN_PATH = uc.get_plugin_path()

sys.path.append(PLUGIN_PATH)
from Model.Page1Model import Page1Model
from Model.Page2Model import Page2Model


@dataclass
class BaseModel:
    def __init__(self):
        self.model1 = None
        self.model2 = None

    @property
    def model1(self) -> Page1Model:
        return self.__model1

    @model1.setter
    def model1(self, value):
        self.__model1 = value

    @property
    def model2(self) -> Page2Model:
        return self.__model2

    @model2.setter
    def model2(self, value):
        self.__model2 = value
