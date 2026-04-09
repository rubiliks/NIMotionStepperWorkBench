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



    def handle_click(self):
        new_value = self.model.increment()
        print(new_value)
