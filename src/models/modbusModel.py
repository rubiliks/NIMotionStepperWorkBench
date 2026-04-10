from PySide6.QtCore import QObject, Slot
from PySide6.QtSerialBus import (QModbusRtuSerialClient, QModbusDataUnit,
                                 QModbusDevice)
from PySide6.QtSerialPort import QSerialPort

class ModbusModel(QObject):

    def __init__(self):
        super().__init__()
        self._counter = 0
        self.client = QModbusRtuSerialClient(self)
        self.client.setConnectionParameter(QModbusDevice.SerialPortNameParameter, "COM3")
        self.client.setConnectionParameter(QModbusDevice.SerialParityParameter, QSerialPort.NoParity)
        self.client.setConnectionParameter(QModbusDevice.SerialBaudRateParameter, QSerialPort.BaudRate.Baud115200)
        self.client.setConnectionParameter(QModbusDevice.SerialDataBitsParameter, QSerialPort.Data8)
        self.client.setConnectionParameter(QModbusDevice.SerialStopBitsParameter, QSerialPort.OneStop)
        self.client.setTimeout(1000)
        self.client.setNumberOfRetries(3)

        if not self.client.connectDevice():
            print(f"Ошибка подключения: {self.client.errorString()}")
        else:
            print("Подключено")

        self.readData()
        self.readImputRegister()





    def writeHolgingRegisterMotor(self,address,register,value):
        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, register, 1)
        write_unit.setValue(0, value)
        reply = self.client.sendWriteRequest(write_unit, address)
        if reply:
            if not reply.isFinished():
                print("Запрос отправлен...")
            else:
                print(f"Ошибка при отправке: {reply.errorString()}")
                reply.deleteLater()
        else:
            print(f"Не удалось отправить запрос: {self.client.errorString()}")


    def enableMotor(self):

        print("enableMotor")
        self.writeHolgingRegisterMotor(1,81,6)
        self.writeHolgingRegisterMotor(1, 81, 7)
        self.readImputRegister()


    def disableMotor(self):
        print("disableMotor")
        self.writeHolgingRegisterMotor(1, 81, 6)
        self.readImputRegister()


    def startMotorForward(self):
        print("startMotorForward")
        self.writeHolgingRegisterMotor(1, 82, 0)
        self.writeHolgingRegisterMotor(1, 81, 15)
        self.readImputRegister()


    def startMotorBackward(self):
        print("startMotorBackward")
        self.writeHolgingRegisterMotor(1, 82, 1)
        self.writeHolgingRegisterMotor(1, 81, 15)
        self.readImputRegister()


    def stopMotor(self):
        print("stopMotor")
        self.writeHolgingRegisterMotor(1, 81, 7)
        self.readImputRegister()



    def speedMotor(self,speedIn):
        print("speedMotor")
        self.writeHolgingRegisterMotor(1, 86, speedIn)
        self.readImputRegister()


    def readImputRegister (self):
        slave_id = 1
        request = QModbusDataUnit(QModbusDataUnit.InputRegisters, 31, 1)
        reply = self.client.sendReadRequest(request, 1)
        if reply:
            while not reply.isFinished():
                from PySide6.QtCore import QCoreApplication
                QCoreApplication.processEvents()
            if reply.error() == QModbusDevice.NoError:
                result = reply.result()
                value = result.value(0)  # Читаем первое (и единственное) значение
                print(f"Регистр {result.startAddress()}: {value}")
            else:
                print(f"Ошибка чтения: {reply.errorString()}")


    def readData (self):
        slave_id = 1
        request = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, 85, 10)
        reply = self.client.sendReadRequest(request, slave_id)

        if reply:
            while not reply.isFinished():
                # В цикле событий Qt это происходит автоматически,
                # здесь мы просто ждем завершения операции
                from PySide6.QtCore import QCoreApplication
                QCoreApplication.processEvents()

            # 4. Проверяем на ошибки и выводим результат
            if reply.error() == QModbusDevice.NoError:
                result = reply.result()
                value = result.value(0)  # Читаем первое (и единственное) значение
                print(f"Регистр {result.startAddress()}: {value}")
            else:
                print(f"Ошибка чтения: {reply.errorString()}")

            if reply.error() == QModbusDevice.NoError:
                result = reply.result()
                value = result.value(1)  # Читаем первое (и единственное) значение
                print(f"Регистр {result.startAddress()}: {value}")
            else:
                print(f"Ошибка чтения: {reply.errorString()}")
            # Очистка
            reply.deleteLater()

