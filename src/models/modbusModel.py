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


    def writeHolgingRegisterMotor(self,address,resister,value):
        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, resister, 1)
        write_unit.setValue(0, value)  # Устанавливаем значение 123 в первый (0-й) элемент
        reply = self.client.sendWriteRequest(write_unit, address)





    def enableMotor(self):
        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, 81, 1)
        write_unit.setValue(0, 6)  # Устанавливаем значение 123 в первый (0-й) элемент

        # 3. Отправляем запрос на Slave ID 1
        reply = self.client.sendWriteRequest(write_unit, 1)

        if reply:
            # Проверка завершения (в реальном GUI приложении лучше через сигналы)
            if not reply.isFinished():
                # Если нужно подождать (только для простых скриптов, не для GUI!)
                # reply.finished.connect(lambda: print("Запись завершена"))
                print("Запрос отправлен...")
            else:
                # Ошибка возникла мгновенно
                print(f"Ошибка при отправке: {reply.errorString()}")
                reply.deleteLater()
        else:
            print(f"Не удалось отправить запрос: {self.client.errorString()}")

        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, 81, 1)
        write_unit.setValue(0, 7)  # Устанавливаем значение 123 в первый (0-й) элемент

        # 3. Отправляем запрос на Slave ID 1
        reply = self.client.sendWriteRequest(write_unit, 1)

        if reply:
            # Проверка завершения (в реальном GUI приложении лучше через сигналы)
            if not reply.isFinished():
                # Если нужно подождать (только для простых скриптов, не для GUI!)
                # reply.finished.connect(lambda: print("Запись завершена"))
                print("Запрос отправлен...")
            else:
                # Ошибка возникла мгновенно
                print(f"Ошибка при отправке: {reply.errorString()}")
                reply.deleteLater()
        else:
            print(f"Не удалось отправить запрос: {self.client.errorString()}")

    def disableMotor(self):
        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, 81, 1)
        write_unit.setValue(0, 6)  # Устанавливаем значение 123 в первый (0-й) элемент

        # 3. Отправляем запрос на Slave ID 1
        reply = self.client.sendWriteRequest(write_unit, 1)

        if reply:
            # Проверка завершения (в реальном GUI приложении лучше через сигналы)
            if not reply.isFinished():
                # Если нужно подождать (только для простых скриптов, не для GUI!)
                # reply.finished.connect(lambda: print("Запись завершена"))
                print("Запрос отправлен...")
            else:
                # Ошибка возникла мгновенно
                print(f"Ошибка при отправке: {reply.errorString()}")
                reply.deleteLater()
        else:
            print(f"Не удалось отправить запрос: {self.client.errorString()}")

    def startMotorForward(self):
        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, 82, 1)
        write_unit.setValue(0, 0)  # Устанавливаем значение 123 в первый (0-й) элемент

        # 3. Отправляем запрос на Slave ID 1
        reply = self.client.sendWriteRequest(write_unit, 1)

        if reply:
            # Проверка завершения (в реальном GUI приложении лучше через сигналы)
            if not reply.isFinished():
                # Если нужно подождать (только для простых скриптов, не для GUI!)
                # reply.finished.connect(lambda: print("Запись завершена"))
                print("Запрос отправлен...")
            else:
                # Ошибка возникла мгновенно
                print(f"Ошибка при отправке: {reply.errorString()}")
                reply.deleteLater()
        else:
            print(f"Не удалось отправить запрос: {self.client.errorString()}")

        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, 81, 1)
        write_unit.setValue(0, 15)  # Устанавливаем значение 123 в первый (0-й) элемент

        # 3. Отправляем запрос на Slave ID 1
        reply = self.client.sendWriteRequest(write_unit, 1)

        if reply:
            # Проверка завершения (в реальном GUI приложении лучше через сигналы)
            if not reply.isFinished():
                # Если нужно подождать (только для простых скриптов, не для GUI!)
                # reply.finished.connect(lambda: print("Запись завершена"))
                print("Запрос отправлен...")
            else:
                # Ошибка возникла мгновенно
                print(f"Ошибка при отправке: {reply.errorString()}")
                reply.deleteLater()
        else:
            print(f"Не удалось отправить запрос: {self.client.errorString()}")

    def startMotorBackward(self):
        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, 82, 1)
        write_unit.setValue(0, 1)  # Устанавливаем значение 123 в первый (0-й) элемент

        # 3. Отправляем запрос на Slave ID 1
        reply = self.client.sendWriteRequest(write_unit, 1)

        if reply:
            # Проверка завершения (в реальном GUI приложении лучше через сигналы)
            if not reply.isFinished():
                # Если нужно подождать (только для простых скриптов, не для GUI!)
                # reply.finished.connect(lambda: print("Запись завершена"))
                print("Запрос отправлен...")
            else:
                # Ошибка возникла мгновенно
                print(f"Ошибка при отправке: {reply.errorString()}")
                reply.deleteLater()
        else:
            print(f"Не удалось отправить запрос: {self.client.errorString()}")

        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, 81, 1)
        write_unit.setValue(0, 15)  # Устанавливаем значение 123 в первый (0-й) элемент

        # 3. Отправляем запрос на Slave ID 1
        reply = self.client.sendWriteRequest(write_unit, 1)

        if reply:
            # Проверка завершения (в реальном GUI приложении лучше через сигналы)
            if not reply.isFinished():
                # Если нужно подождать (только для простых скриптов, не для GUI!)
                # reply.finished.connect(lambda: print("Запись завершена"))
                print("Запрос отправлен...")
            else:
                # Ошибка возникла мгновенно
                print(f"Ошибка при отправке: {reply.errorString()}")
                reply.deleteLater()
        else:
            print(f"Не удалось отправить запрос: {self.client.errorString()}")

    def stopMotor(self):
        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, 81, 1)
        write_unit.setValue(0, 7)  # Устанавливаем значение 123 в первый (0-й) элемент

        # 3. Отправляем запрос на Slave ID 1
        reply = self.client.sendWriteRequest(write_unit, 1)

        if reply:
            # Проверка завершения (в реальном GUI приложении лучше через сигналы)
            if not reply.isFinished():
                # Если нужно подождать (только для простых скриптов, не для GUI!)
                # reply.finished.connect(lambda: print("Запись завершена"))
                print("Запрос отправлен...")
            else:
                # Ошибка возникла мгновенно
                print(f"Ошибка при отправке: {reply.errorString()}")
                reply.deleteLater()
        else:
            print(f"Не удалось отправить запрос: {self.client.errorString()}")

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

    def speedMotor(self,speedIn):
        write_unit = QModbusDataUnit(QModbusDataUnit.HoldingRegisters, 86, 1)
        write_unit.setValue(0, speedIn)  # Устанавливаем значение 123 в первый (0-й) элемент

        # 3. Отправляем запрос на Slave ID 1
        reply = self.client.sendWriteRequest(write_unit, 1)

        if reply:
            # Проверка завершения (в реальном GUI приложении лучше через сигналы)
            if not reply.isFinished():
                # Если нужно подождать (только для простых скриптов, не для GUI!)
                # reply.finished.connect(lambda: print("Запись завершена"))
                print("Запрос отправлен...")
            else:
                # Ошибка возникла мгновенно
                print(f"Ошибка при отправке: {reply.errorString()}")
                reply.deleteLater()
        else:
            print(f"Не удалось отправить запрос: {self.client.errorString()}")




