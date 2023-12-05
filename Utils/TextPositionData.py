import cadwork


class TextPositionData:
    def __init__(self, position: cadwork.point_3d, xl: cadwork.point_3d, zl: cadwork.point_3d):
        self.__position = position
        self.__xl = xl
        self.__zl = zl

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def xl(self):
        return self.__xl

    @xl.setter
    def xl(self, value):
        self.__xl = value

    @property
    def zl(self):
        return self.__zl

    @zl.setter
    def zl(self, value):
        self.__zl = value


def create_text_position_data() -> TextPositionData:
    position = cadwork.point_3d(0., 0., 0.)
    xl = cadwork.point_3d(1., 0., 0.)
    zl = cadwork.point_3d(0., 0., 1.)
    return TextPositionData(position, xl, zl)


def create_text_option_data(text: str, element_type: cadwork.text_object_options):
    text_options = cadwork.text_object_options()
    text_options.set_color(5)
    text_options.set_element_type(element_type)
    text_options.set_text(text)
    text_options.set_height(100.0)
    text_options.set_thickness(5.0)

    return text_options
