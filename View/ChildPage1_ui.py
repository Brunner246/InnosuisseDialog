# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ChildPage1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbn_path = QtWidgets.QPushButton(Form)
        self.pbn_path.setObjectName("pbn_path")
        self.horizontalLayout.addWidget(self.pbn_path)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.spb_count = QtWidgets.QSpinBox(Form)
        self.spb_count.setMaximum(2000)
        self.spb_count.setObjectName("spb_count")
        self.verticalLayout.addWidget(self.spb_count)
        self.led_text = QtWidgets.QLineEdit(Form)
        self.led_text.setObjectName("led_text")
        self.verticalLayout.addWidget(self.led_text)
        self.cbx_geometry_type = QtWidgets.QComboBox(Form)
        self.cbx_geometry_type.setObjectName("cbx_geometry_type")
        self.verticalLayout.addWidget(self.cbx_geometry_type)
        self.pbn_text_object = QtWidgets.QPushButton(Form)
        self.pbn_text_object.setObjectName("pbn_text_object")
        self.verticalLayout.addWidget(self.pbn_text_object)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pbn_test_button = QtWidgets.QPushButton(Form)
        self.pbn_test_button.setObjectName("pbn_test_button")
        self.horizontalLayout.addWidget(self.pbn_test_button)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pbn_path.setText(_translate("Form", "print path"))
        self.spb_count.setSuffix(_translate("Form", " items"))
        self.led_text.setPlaceholderText(_translate("Form", "write a text"))
        self.pbn_text_object.setText(_translate("Form", "create text object"))
        self.pbn_test_button.setText(_translate("Form", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
