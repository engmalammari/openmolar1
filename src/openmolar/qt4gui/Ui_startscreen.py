# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openmolar/openmolar/src/openmolar/qt-designer/startscreen.ui'
#
# Created: Thu Sep 24 21:16:21 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(232, 320)
        Dialog.setMinimumSize(QtCore.QSize(200, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/openmolar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.password_lineEdit.setMaximumSize(QtCore.QSize(71, 16777215))
        self.password_lineEdit.setMaxLength(10)
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout_2.addWidget(self.password_lineEdit, 0, 1, 1, 1)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.user1_lineEdit = QtGui.QLineEdit(Dialog)
        self.user1_lineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.user1_lineEdit.setMaxLength(6)
        self.user1_lineEdit.setObjectName("user1_lineEdit")
        self.gridLayout.addWidget(self.user1_lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.user2_lineEdit = QtGui.QLineEdit(Dialog)
        self.user2_lineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
        self.user2_lineEdit.setMaxLength(6)
        self.user2_lineEdit.setObjectName("user2_lineEdit")
        self.gridLayout.addWidget(self.user2_lineEdit, 1, 1, 1, 1)
        self.surgery_radioButton = QtGui.QRadioButton(Dialog)
        self.surgery_radioButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.surgery_radioButton.setChecked(True)
        self.surgery_radioButton.setObjectName("surgery_radioButton")
        self.gridLayout.addWidget(self.surgery_radioButton, 2, 0, 1, 2)
        self.reception_radioButton = QtGui.QRadioButton(Dialog)
        self.reception_radioButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.reception_radioButton.setObjectName("reception_radioButton")
        self.gridLayout.addWidget(self.reception_radioButton, 3, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 6, 0, 1, 2)
        self.options_frame = QtGui.QFrame(Dialog)
        self.options_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.options_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.options_frame.setObjectName("options_frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.options_frame)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setMargin(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtGui.QLabel(self.options_frame)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.server_comboBox = QtGui.QComboBox(self.options_frame)
        self.server_comboBox.setObjectName("server_comboBox")
        self.verticalLayout.addWidget(self.server_comboBox)
        self.gridLayout_2.addWidget(self.options_frame, 3, 0, 1, 2)
        self.options_pushButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.options_pushButton.sizePolicy().hasHeightForWidth())
        self.options_pushButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.options_pushButton.setIcon(icon1)
        self.options_pushButton.setObjectName("options_pushButton")
        self.gridLayout_2.addWidget(self.options_pushButton, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "openMolar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "System Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "User 1(required)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "User 2 (optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.surgery_radioButton.setText(QtGui.QApplication.translate("Dialog", "Surgery Machine", None, QtGui.QApplication.UnicodeUTF8))
        self.reception_radioButton.setText(QtGui.QApplication.translate("Dialog", "Reception Machine", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Chose a server", None, QtGui.QApplication.UnicodeUTF8))
        self.options_pushButton.setText(QtGui.QApplication.translate("Dialog", "Show Advanced Options", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
