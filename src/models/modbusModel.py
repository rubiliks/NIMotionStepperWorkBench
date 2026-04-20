import gc
import time

from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtSerialBus import (QModbusRtuSerialClient, QModbusDataUnit, QModbusDevice)
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import Signal
from PySide6.QtCore import QTimer

class ModbusModel(QObject):
    dataRecrived = Signal(float)
    dataConnectionStatus =  Signal(bool)
    dataGate1Status = Signal(bool)
    dataGate2Status = Signal(bool)

    def __init__(self):
        super().__init__()
        self._modbus_device = None
        self._modbus_device = QModbusRtuSerialClient(self)
        self.timer = QTimer()
        self.timer.timeout.connect(lambda:self.readImputRegister(1,31))

        self.timer2 = QTimer()
        self.timer2.timeout.connect(lambda:self.readImputRegister(1,24))

    # Соединение модбас
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
                self.timer.stop()
                self.timer2.stop()
            else:
                print("Подключено")
                self.dataConnectionStatus.emit(True)
                self.timer.start(200)
                self.timer2.start(200)

        else:
            self._modbus_device.disconnectDevice()
            print("Соединение разорвано")
            self.dataConnectionStatus.emit(False)
            self.timer.stop()
            self.timer2.stop()

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
            print(f"Ошибка при записи: (код: {error})")
        reply.deleteLater()

    # Чтение регистров
    def readImputRegister (self, address, register):
        request = QModbusDataUnit(QModbusDataUnit.InputRegisters, register, 1)
        reply = self._modbus_device.sendReadRequest(request, address)
        if reply:
            reply.finished.connect(self._read_finished)
            print(f"Запрос на чтение отправлен")
        else:
            print(f"Не удалось отправить запрос на чтение: {self._modbus_device.errorString()}")

    def _read_finished(self):
        reply = self.sender()
        if not reply:
            return
        error = reply.error()
        if error == QModbusDevice.NoError:
            result = reply.result()
            if result.valueCount() > 0:
                value = result.value(0)
                register = result.startAddress()
                print(f"Регистр {register}: {value}")
                if register == 24:
                    self.print_bits_lsb(value)
                if register == 31:
                    self.dataRecrived.emit(value)

            else:
                print("Нет данных в ответе")
        elif error == QModbusDevice.ProtocolError:
            ex = reply.rawResult().exceptionCode()
            print(f"Ошибка протокола Modbus (код исключения: 0x{ex:x})")
        else:
            print(f"Ошибка при чтении: {reply.errorString()} (код: {error})")
        reply.deleteLater()


    # Управление двигателем

    def enableMotor(self):
        print("enableMotor")
        self.writeHolgingRegisterMotor(1,81,6)
        self.writeHolgingRegisterMotor(1, 81, 7)

    def disableMotor(self):
        print("disableMotor")
        self.writeHolgingRegisterMotor(1, 81, 6)

    def startMotorForward(self):
        print("startMotorForward")
        self.writeHolgingRegisterMotor(1, 82, 0)
        self.writeHolgingRegisterMotor(1, 81, 15)

    def startMotorBackward(self):
        print("startMotorBackward")
        self.writeHolgingRegisterMotor(1, 82, 1)
        self.writeHolgingRegisterMotor(1, 81, 15)

    def stopMotor(self):
        print("stopMotor")
        self.writeHolgingRegisterMotor(1, 81, 7)

    def speedMotor(self,speedIn):
        print("speedMotor")
        self.writeHolgingRegisterMotor(1, 86, speedIn)

    def print_bits_lsb(self,value, bits=2):
        print(f"Число: {value}")
        for i in range(bits):
            bit = (value >> i) & 1
            print(f"Бит {i:2d}: {bit}")
            if i == 0:
                self.dataGate1Status.emit(bit)
            if i == 1:
                self.dataGate2Status.emit(bit)



