from time import sleep
from pySerialTransfer import pySerialTransfer



class SensorsReader:

    def convertRawReading(self):

        self.Readings["temp0"]=self.RawReadings["temp0"]
        self.Readings["temp1"]=self.RawReadings["temp1"]
        self.Readings["temp2"]=self.RawReadings["temp2"]
        self.Readings["temp3"]=self.RawReadings["temp3"]

        self.Readings["temp4"]=self.RawReadings["temp4"]
        self.Readings["temp5"]=self.RawReadings["temp5"]
        self.Readings["temp6"]=self.RawReadings["temp6"]
        self.Readings["temp7"]=self.RawReadings["temp7"]

        self.Readings["pressure0"]=self.RawReadings["analog0"]/1024*5
        self.Readings["pressure1"]=self.RawReadings["analog1"]/1024*5
        self.Readings["pressure2"]=self.RawReadings["analog2"]/1024*5
        self.Readings["pressure3"]=self.RawReadings["analog3"]/1024*5

        self.Readings["flowRate0"]=self.RawReadings["interruptRate0"]*60/5.5
        self.Readings["flowRate1"]=self.RawReadings["interruptRate1"]*60/5.5
        

    def __init__(self, comport) -> None:
        self.RawReadings = {
            "temp0": 0,
            "temp1": 0,
            "temp2": 0,
            "temp3": 0,

            "temp4": 0,
            "temp5": 0,
            "temp6": 0,
            "temp7": 0,

            "analog0": 0,
            "analog1": 0,
            "analog2": 0,
            "analog3": 0,

            "interruptRate0": 0,
            "interruptRate1": 0
        }

        self.Readings = {
            "temp0": 0,
            "temp1": 0,
            "temp2": 0,
            "temp3": 0,

            "temp4": 0,
            "temp5": 0,
            "temp6": 0,
            "temp7": 0,

            "pressure0": 0,
            "pressure1": 0,
            "pressure2": 0,
            "pressure3": 0,

            "flowRate0": 0,
            "flowRate1": 0
        }     


        self.comport = comport

        try:
            print(f'Connecting to {self.comport}')
            self.link = pySerialTransfer.SerialTransfer(self.comport)
            print(f'Connected to {self.comport}')

        except pySerialTransfer.InvalidSerialPort as e:
            print(f'Error Connecting to {self.comport}')
            self.comport = pySerialTransfer.serial_ports()[0]
            print(f'Connecting to {self.comport}')
            self.link = pySerialTransfer.SerialTransfer(self.comport)
            print(f'Connected to {self.comport}')

        self.link.open()
        sleep(1)

    def printRawReadings(self):

        print('----- Sensor Raw Readings -----')

        print('----- Temperature Sensors (Centigrade) -----')
        print(f'{self.RawReadings["temp0"]}, {self.RawReadings["temp1"]}, {self.RawReadings["temp2"]}, {self.RawReadings["temp3"]}, {self.RawReadings["temp4"]}, {self.RawReadings["temp5"]}, {self.RawReadings["temp6"]}, {self.RawReadings["temp7"]}')

        print('----- Pressure Sensors (10 bit Analog Read) -----')
        print(
            f'{self.RawReadings["analog0"]}, {self.RawReadings["analog1"]}, {self.RawReadings["analog2"]}, {self.RawReadings["analog3"]}')

        print('----- Flow Sensors (Interrupts Per Seconds) -----')
        print(
            f'{self.RawReadings["interruptRate0"]}, {self.RawReadings["interruptRate1"]}')
        
    def printReadings(self):

        print('----- Sensor Readings -----')

        print('----- Temperature Sensors (Centigrade) -----')
        print(f'{self.Readings["temp0"]}, {self.Readings["temp1"]}, {self.Readings["temp2"]}, {self.Readings["temp3"]}, {self.Readings["temp4"]}, {self.Readings["temp5"]}, {self.Readings["temp6"]}, {self.Readings["temp7"]}')

        print('----- Pressure Sensors (KPIa) -----')
        print(
            f'{self.Readings["pressure0"]}, {self.Readings["pressure1"]}, {self.Readings["pressure2"]}, {self.Readings["pressure3"]}')

        print('----- Flow Sensors (LPM) -----')
        print(
            f'{self.Readings["flowRate0"]}, {self.Readings["flowRate1"]}')
        
    def read(self):

        # try:

        if self.link.available():
            recSize = 0

            self.RawReadings["temp0"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["temp1"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["temp2"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["temp3"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["temp4"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["temp5"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["temp6"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["temp7"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["analog0"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["analog1"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["analog2"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["analog3"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["interruptRate0"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            self.RawReadings["interruptRate1"] = self.link.rx_obj(
                obj_type='f', start_pos=recSize)
            recSize += pySerialTransfer.STRUCT_FORMAT_LENGTHS['f']

            return True

        elif self.link.status < 0:
            if self.link.status == pySerialTransfer.CRC_ERROR:
                print('ERROR: CRC_ERROR')
            elif self.link.status == pySerialTransfer.PAYLOAD_ERROR:
                print('ERROR: PAYLOAD_ERROR')
            elif self.link.status == pySerialTransfer.STOP_BYTE_ERROR:
                print('ERROR: STOP_BYTE_ERROR')
            else:
                print('ERROR: {}'.format(self.link.status))

        # except KeyboardInterrupt:
        #     self.link.close()

        return False
        

    def getRawReadings(self):
        return self.RawReadings
    
    def getReadings(self):
        return self.Readings
