# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openmolar/openmolar/src/openmolar/qt-designer/chooseDocument.ui'
#
# Created: Wed Sep 30 16:09:49 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(394, 195)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.remuneration_radioButton = QtGui.QRadioButton(self.tab)
        self.remuneration_radioButton.setChecked(True)
        self.remuneration_radioButton.setObjectName("remuneration_radioButton")
        self.verticalLayout_2.addWidget(self.remuneration_radioButton)
        self.info_radioButton = QtGui.QRadioButton(self.tab)
        self.info_radioButton.setObjectName("info_radioButton")
        self.verticalLayout_2.addWidget(self.info_radioButton)
        spacerItem = QtGui.QSpacerItem(128, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.remuneration2009_radioButton = QtGui.QRadioButton(self.tab_2)
        self.remuneration2009_radioButton.setChecked(True)
        self.remuneration2009_radioButton.setObjectName("remuneration2009_radioButton")
        self.verticalLayout_3.addWidget(self.remuneration2009_radioButton)
        self.info2009_radioButton = QtGui.QRadioButton(self.tab_2)
        self.info2009_radioButton.setObjectName("info2009_radioButton")
        self.verticalLayout_3.addWidget(self.info2009_radioButton)
        spacerItem1 = QtGui.QSpacerItem(128, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Choose a Document", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Choose a document to view", None, QtGui.QApplication.UnicodeUTF8))
        self.remuneration_radioButton.setText(QtGui.QApplication.translate("Dialog", "NHS Schedule of Remuneration April 2008", None, QtGui.QApplication.UnicodeUTF8))
        self.info_radioButton.setText(QtGui.QApplication.translate("Dialog", "NHS \"Information Guide\" 2008", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "2008", None, QtGui.QApplication.UnicodeUTF8))
        self.remuneration2009_radioButton.setText(QtGui.QApplication.translate("Dialog", "NHS Schedule of Remuneration", None, QtGui.QApplication.UnicodeUTF8))
        self.info2009_radioButton.setText(QtGui.QApplication.translate("Dialog", "NHS \"Information Guide\"", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "2009", None, QtGui.QApplication.UnicodeUTF8))
