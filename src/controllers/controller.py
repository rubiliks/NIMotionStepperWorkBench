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

        self.ui.MotorStart_PushButton.clicked.connect(self.modbusModel.startMotorForward)
        self.ui.pushButton_3.clicked.connect(self.modbusModel.startMotorBackward)
        self.ui.MotorStop_PushButton.clicked.connect(self.modbusModel.stopMotor)

        self.ui.MotorEnable_pushButton.clicked.connect(self.modbusModel.enableMotor)
        self.ui.MotorDisable_pushButton.clicked.connect(self.modbusModel.disableMotor)

        self.ui.MotorSpeed_DoubleSpinBox.setMaximum(500.0)
        self.ui.MotorSpeed_DoubleSpinBox.setValue(100)
        self.modbusModel.speedMotor(100)

        self.ui.MotorSpeed_DoubleSpinBox.valueChanged.connect(self.modbusModel.speedMotor)

    def handle_click(self):
        new_value = self.model.increment()
        print(new_value)
