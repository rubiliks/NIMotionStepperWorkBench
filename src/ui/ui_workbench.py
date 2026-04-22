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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(404, 335)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Modbus_connection_label = QLabel(self.centralwidget)
        self.Modbus_connection_label.setObjectName(u"Modbus_connection_label")

        self.horizontalLayout_6.addWidget(self.Modbus_connection_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Modbus_status_word_lineEdit = QLineEdit(self.centralwidget)
        self.Modbus_status_word_lineEdit.setObjectName(u"Modbus_status_word_lineEdit")
        self.Modbus_status_word_lineEdit.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Modbus_status_word_lineEdit.sizePolicy().hasHeightForWidth())
        self.Modbus_status_word_lineEdit.setSizePolicy(sizePolicy1)
        self.Modbus_status_word_lineEdit.setMaximumSize(QSize(16777213, 16777215))

        self.horizontalLayout_12.addWidget(self.Modbus_status_word_lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Modbus_con_discon_pushButton = QPushButton(self.centralwidget)
        self.Modbus_con_discon_pushButton.setObjectName(u"Modbus_con_discon_pushButton")

        self.horizontalLayout_8.addWidget(self.Modbus_con_discon_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Motor_status_word_label_2 = QLabel(self.centralwidget)
        self.Motor_status_word_label_2.setObjectName(u"Motor_status_word_label_2")
        self.Motor_status_word_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.Motor_status_word_label_2)

        self.Motor_status_word_lineEdit = QLineEdit(self.centralwidget)
        self.Motor_status_word_lineEdit.setObjectName(u"Motor_status_word_lineEdit")
        self.Motor_status_word_lineEdit.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.Motor_status_word_lineEdit.sizePolicy().hasHeightForWidth())
        self.Motor_status_word_lineEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.Motor_status_word_lineEdit)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.MotorEnable_pushButton = QPushButton(self.centralwidget)
        self.MotorEnable_pushButton.setObjectName(u"MotorEnable_pushButton")

        self.horizontalLayout_9.addWidget(self.MotorEnable_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.MotorDisable_pushButton = QPushButton(self.centralwidget)
        self.MotorDisable_pushButton.setObjectName(u"MotorDisable_pushButton")

        self.horizontalLayout_10.addWidget(self.MotorDisable_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.MotorStartForward_PushButton = QPushButton(self.centralwidget)
        self.MotorStartForward_PushButton.setObjectName(u"MotorStartForward_PushButton")

        self.horizontalLayout_4.addWidget(self.MotorStartForward_PushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.MotorStartBackward_PushButton = QPushButton(self.centralwidget)
        self.MotorStartBackward_PushButton.setObjectName(u"MotorStartBackward_PushButton")

        self.horizontalLayout_11.addWidget(self.MotorStartBackward_PushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

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

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.gate_sensor_1_label = QLabel(self.centralwidget)
        self.gate_sensor_1_label.setObjectName(u"gate_sensor_1_label")

        self.horizontalLayout_14.addWidget(self.gate_sensor_1_label)

        self.gate_sensor_1_indicator = QLabel(self.centralwidget)
        self.gate_sensor_1_indicator.setObjectName(u"gate_sensor_1_indicator")

        self.horizontalLayout_14.addWidget(self.gate_sensor_1_indicator)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.gate_sensor_2_label = QLabel(self.centralwidget)
        self.gate_sensor_2_label.setObjectName(u"gate_sensor_2_label")

        self.horizontalLayout_15.addWidget(self.gate_sensor_2_label)

        self.gate_sensor_2_indicator = QLabel(self.centralwidget)
        self.gate_sensor_2_indicator.setObjectName(u"gate_sensor_2_indicator")
        self.gate_sensor_2_indicator.setAutoFillBackground(False)

        self.horizontalLayout_15.addWidget(self.gate_sensor_2_indicator)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 404, 22))
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
        self.Modbus_connection_label.setText(QCoreApplication.translate("MainWindow", u"Modbus connection", None))
        self.Modbus_con_discon_pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect/disconect", None))
        self.Motor_status_word_label_2.setText(QCoreApplication.translate("MainWindow", u"Motor control", None))
        self.Motor_status_word_lineEdit.setText("")
        self.MotorEnable_pushButton.setText(QCoreApplication.translate("MainWindow", u"Enable Motor", None))
        self.MotorDisable_pushButton.setText(QCoreApplication.translate("MainWindow", u"Disable Motor", None))
        self.MotorStartForward_PushButton.setText(QCoreApplication.translate("MainWindow", u"Start motor forward", None))
        self.MotorStartBackward_PushButton.setText(QCoreApplication.translate("MainWindow", u"Start motor backward", None))
        self.MotorStop_PushButton.setText(QCoreApplication.translate("MainWindow", u"Stop motor", None))
        self.ErrorAcknow_PushButton.setText(QCoreApplication.translate("MainWindow", u"Error acknowledg", None))
        self.MotorSpeed_Label.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Work bench", None))
        self.gate_sensor_1_label.setText(QCoreApplication.translate("MainWindow", u"Gate sensor 1", None))
        self.gate_sensor_1_indicator.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.gate_sensor_2_label.setText(QCoreApplication.translate("MainWindow", u"Gate sensor 2", None))
        self.gate_sensor_2_indicator.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
    # retranslateUi

