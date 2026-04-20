from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from src.models.model import MainModel
from src.models.modbusModel import ModbusModel
from src.ui.ui_workbench import Ui_MainWindow


class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = MainModel()
        self.modbusModel = ModbusModel()

        #Button connection
        self.ui.Modbus_con_discon_pushButton.clicked.connect(self.modbusModel.connectModbus)

        #Button motor
        self.ui.MotorStartForward_PushButton.clicked.connect(self.modbusModel.startMotorForward)
        self.ui.MotorStartBackward_PushButton.clicked.connect(self.modbusModel.startMotorBackward)

        self.ui.MotorStop_PushButton.clicked.connect(self.modbusModel.stopMotor)
        self.ui.MotorEnable_pushButton.clicked.connect(self.modbusModel.enableMotor)
        self.ui.MotorDisable_pushButton.clicked.connect(self.modbusModel.disableMotor)

        # Speed connection / setting
        self.ui.MotorSpeed_DoubleSpinBox.setMaximum(500.0)
        self.ui.MotorSpeed_DoubleSpinBox.setValue(100)
        self.ui.MotorSpeed_DoubleSpinBox.valueChanged.connect(self.modbusModel.speedMotor)
#        self.modbusModel.speedMotor(100)

        #Status motor connection
        self.modbusModel.dataRecrived.connect(self.updateMotorStatusLabel)
        self.ui.Motor_status_word_lineEdit.setEnabled(False)

        #Status connection
        self.modbusModel.dataConnectionStatus.connect(self.updateconnectStatusLabel)

        # Gate indicator
        self.ui.gate_sensor_1_indicator.setStyleSheet(""" background-color: red; border: 1px solid black;""")
        self.ui.gate_sensor_2_indicator.setStyleSheet(""" background-color: red; border: 1px solid black;""")
        self.ui.gate_sensor_1_indicator.setText("               ")
        self.ui.gate_sensor_2_indicator.setText("               ")

        self.modbusModel.dataGate1Status.connect(self.updateGate1StatusLabel)
        self.modbusModel.dataGate2Status.connect(self.updateGate2StatusLabel)

    def updateMotorStatusLabel(self, value):
        self.ui.Motor_status_word_lineEdit.setText(str(value))

    def updateconnectStatusLabel(self, value):
        self.ui.Modbus_status_word_lineEdit.setText(str(value))

    def updateGate1StatusLabel(self, value):
        if value == 0:
            self.ui.gate_sensor_1_indicator.setStyleSheet(""" background-color: red; border: 1px solid black;""")
        if value == 1:
            self.ui.gate_sensor_1_indicator.setStyleSheet(""" background-color: green; border: 1px solid black;""")

    def updateGate2StatusLabel(self, value):
        if value == 0:
            self.ui.gate_sensor_2_indicator.setStyleSheet(""" background-color: red; border: 1px solid black;""")
        if value == 1:
            self.ui.gate_sensor_2_indicator.setStyleSheet(""" background-color: green; border: 1px solid black;""")
