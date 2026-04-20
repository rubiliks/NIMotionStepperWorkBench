import gc
import time

from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtSerialBus import (QModbusRtuSerialClient, QModbusDataUnit,
                                 QModbusDevice)
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import Signal

class ModbusModel(QObject):
    dataRecrived = Signal(float)
    dataConnectionStatus =  Signal(bool)

    def __init__(self):
        super().__init__()

        self._modbus_device = None
        self._modbus_device = QModbusRtuSerialClient(self)


    def connectModbus (self):
        if self._modbus_device.state() != QModbusDevice.State.ConnectedState:
            self._modbus_device.setConnectionParameter(QModbusDevice.SerialPortNameParameter, "COM3")
            self._modbus_device.setConnectionParameter(QModbusDevice.SerialParityParameter, QSerialPort.NoParity)
            self._modbus_device.setConnectionParameter(QModbusDevice.SerialBaudRateParameter, QSerialPort.BaudRate.Baud115200)
            self._modbus_device.setConnectionParameter(QModbusDevice.SerialDataBitsParameter, QSerialPort.Data8)
            self._modbus_device.setConnectionParameter(QModbusDevice.SerialStopBitsParameter, QSerialPort.OneStop)
            self._modbus_device.setTimeout(100)
            self._modbus_device.setNumberOfRetries(3)
            if not self._modbus_device.connectDevice():
                print(f"Ошибка подключения: {self._modbus_device.errorString()}")
                self.dataConnectionStatus.emit(False)
            else:
                print("Подключено")
                self.dataConnectionStatus.emit(True)
        else:
            self._modbus_device.disconnectDevice()
            print("Соединение разорвано")
            self.dataConnectionStatus.emit(False)



    # Запись регистров
    def writeHolgingRegisterMotor(self, address, register, value):
        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, register, 1)
        write_unit.setValue(0, value)
        reply = self._modbus_device.sendWriteRequest(write_unit, address)
        if reply:
            reply.finished.connect(self._write_finished)
            print(f"Запрос на запись отправлен (адрес={address}, регистр={register}, значение={value})")
        else:
            print(f"Не удалось отправить запрос: {self._modbus_device.errorString()}")

    def _write_finished(self):
        reply = self.sender()
        if not reply:
            return
        error = reply.error()
        if error == QModbusDevice.NoError:
            print("Запись успешно выполнена")
        elif error == QModbusDevice.ProtocolError:
            ex = reply.rawResult().exceptionCode()
            print(f"Ошибка протокола Modbus (код исключения: 0x{ex:x})")
        else:
            print(f"Ошибка при записи: {reply.errorString()} (код: {error})")
        reply.deleteLater()


    # Чтение регистров
    def readImputRegister (self):
        slave_id = 1
        value = 1
        request = QModbusDataUnit(QModbusDataUnit.InputRegisters, 31, 1)
        reply = self._modbus_device.sendReadRequest(request, 1)
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
        return value










    def enableMotor(self):
        print("enableMotor")
        self.writeHolgingRegisterMotor(1,81,6)
        self.writeHolgingRegisterMotor(1, 81, 7)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)


    def disableMotor(self):
        print("disableMotor")
        self.writeHolgingRegisterMotor(1, 81, 6)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)

    def startMotorForward(self):
        print("startMotorForward")
        self.writeHolgingRegisterMotor(1, 82, 0)
        self.writeHolgingRegisterMotor(1, 81, 15)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)


    def startMotorBackward(self):
        print("startMotorBackward")
        self.writeHolgingRegisterMotor(1, 82, 1)
        self.writeHolgingRegisterMotor(1, 81, 15)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)


    def stopMotor(self):
        print("stopMotor")
        self.writeHolgingRegisterMotor(1, 81, 7)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)


    def speedMotor(self,speedIn):
        print("speedMotor")
        self.writeHolgingRegisterMotor(1, 86, speedIn)
        temp = self.readImputRegister()
        self.dataRecrived.emit(temp)





    def readData (self):
        slave_id = 1
        request = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, 85, 10)
        reply = self._modbus_device.sendReadRequest(request, slave_id)

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

            if reply.error() == QModbusDevice.NoError:
                result = reply.result()
                value = result.value(1)  # Читаем первое (и единственное) значение
                print(f"Регистр {result.startAddress()}: {value}")
            else:
                print(f"Ошибка чтения: {reply.errorString()}")
            # Очистка
            reply.deleteLater()



