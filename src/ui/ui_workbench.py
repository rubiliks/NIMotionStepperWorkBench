# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_workbench.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 524)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 0))
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Motor_status_word_label = QLabel(self.centralwidget)
        self.Motor_status_word_label.setObjectName(u"Motor_status_word_label")

        self.horizontalLayout_6.addWidget(self.Motor_status_word_label)

        self.Motor_status_word_lineEdit = QLineEdit(self.centralwidget)
        self.Motor_status_word_lineEdit.setObjectName(u"Motor_status_word_lineEdit")
        self.Motor_status_word_lineEdit.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Motor_status_word_lineEdit.sizePolicy().hasHeightForWidth())
        self.Motor_status_word_lineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.Motor_status_word_lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Connection_status_radioButton = QRadioButton(self.centralwidget)
        self.Connection_status_radioButton.setObjectName(u"Connection_status_radioButton")

        self.horizontalLayout_8.addWidget(self.Connection_status_radioButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.MotorStart_PushButton = QPushButton(self.centralwidget)
        self.MotorStart_PushButton.setObjectName(u"MotorStart_PushButton")

        self.horizontalLayout_4.addWidget(self.MotorStart_PushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.MotorStop_PushButton = QPushButton(self.centralwidget)
        self.MotorStop_PushButton.setObjectName(u"MotorStop_PushButton")

        self.horizontalLayout_3.addWidget(self.MotorStop_PushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ErrorAcknow_PushButton = QPushButton(self.centralwidget)
        self.ErrorAcknow_PushButton.setObjectName(u"ErrorAcknow_PushButton")

        self.horizontalLayout_7.addWidget(self.ErrorAcknow_PushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.MotorDirection_CheckBox = QCheckBox(self.centralwidget)
        self.MotorDirection_CheckBox.setObjectName(u"MotorDirection_CheckBox")

        self.horizontalLayout_5.addWidget(self.MotorDirection_CheckBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.MotorSpeed_Label = QLabel(self.centralwidget)
        self.MotorSpeed_Label.setObjectName(u"MotorSpeed_Label")

        self.horizontalLayout_2.addWidget(self.MotorSpeed_Label)

        self.MotorSpeed_DoubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.MotorSpeed_DoubleSpinBox.setObjectName(u"MotorSpeed_DoubleSpinBox")

        self.horizontalLayout_2.addWidget(self.MotorSpeed_DoubleSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName(u"menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Motor_status_word_label.setText(QCoreApplication.translate("MainWindow", u"Motor status word", None))
        self.Motor_status_word_lineEdit.setText("")
        self.Connection_status_radioButton.setText(QCoreApplication.translate("MainWindow", u"Connection ok", None))
        self.MotorStart_PushButton.setText(QCoreApplication.translate("MainWindow", u"Start motor", None))
        self.MotorStop_PushButton.setText(QCoreApplication.translate("MainWindow", u"Stop motor", None))
        self.ErrorAcknow_PushButton.setText(QCoreApplication.translate("MainWindow", u"Error acknowledg", None))
        self.MotorDirection_CheckBox.setText(QCoreApplication.translate("MainWindow", u"Direction ", None))
        self.MotorSpeed_Label.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
    # retranslateUi

