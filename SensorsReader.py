from time import sleep
from pySerialTransfer import pySerialTransfer



class SensorsReader:

    def convertRawReading(self):

        self.CalibratedReadings["temp0"]=self.RawReadings["temp0"]
        self.CalibratedReadings["temp1"]=self.RawReadings["temp1"]
        self.CalibratedReadings["temp2"]=self.RawReadings["temp2"]
        self.CalibratedReadings["temp3"]=self.RawReadings["temp3"]

        self.CalibratedReadings["temp4"]=self.RawReadings["temp4"]
        self.CalibratedReadings["temp5"]=self.RawReadings["temp5"]
        self.CalibratedReadings["temp6"]=self.RawReadings["temp6"]
        self.CalibratedReadings["temp7"]=self.RawReadings["temp7"]

        self.CalibratedReadings["pressure0"]=((self.RawReadings["analog0"]/1024*5)-0.5)/4*1200
        self.CalibratedReadings["pressure1"]=((self.RawReadings["analog1"]/1024*5)-0.5)/4*1200
        self.CalibratedReadings["pressure2"]=((self.RawReadings["analog2"]/1024*5)-0.5)/4*1200
        self.CalibratedReadings["pressure3"]=((self.RawReadings["analog3"]/1024*5)-0.5)/4*1200

        self.CalibratedReadings["flowRate0"]=self.RawReadings["interruptRate0"]*60/5.5
        self.CalibratedReadings["flowRate1"]=self.RawReadings["interruptRate1"]*60/5.5


        print('----- Temperature Sensors (Centigrade) -----')
        print(f' Tube In: {self.CalibratedReadings["temp4"]}')
        print(f' Tube Out: {self.CalibratedReadings["temp6"]}')

        print(f' Shell In: {self.CalibratedReadings["temp0"]}')
        print(f' Shell 1: {self.CalibratedReadings["temp3"]}')
        print(f' Shell 2: {self.CalibratedReadings["temp7"]}')
        print(f' Shell 3: {self.CalibratedReadings["temp1"]}')
        print(f' Shell 4: {self.CalibratedReadings["temp5"]}')
        print(f' Shell Out: {self.CalibratedReadings["temp2"]}')


    def LabelReading(self):

        self.LabelledReadings["tempTubeIn"]=self.CalibratedReadings["temp5"]
        self.LabelledReadings["tempTubeOut"]=self.CalibratedReadings["temp6"]

        self.LabelledReadings["tempShellIn"]=self.CalibratedReadings["temp0"]
        self.LabelledReadings["tempShell1"]=self.CalibratedReadings["temp4"]
        self.LabelledReadings["tempShell2"]=self.CalibratedReadings["temp3"]
        self.LabelledReadings["tempShell3"]=self.CalibratedReadings["temp2"]
        self.LabelledReadings["tempShell4"]=self.CalibratedReadings["temp1"]
        self.LabelledReadings["tempShellOut"]=self.CalibratedReadings["temp7"]

        self.LabelledReadings["pressureTubeIn"]=self.CalibratedReadings["pressure0"]
        self.LabelledReadings["pressureTubeOut"]=self.CalibratedReadings["pressure3"]
        self.LabelledReadings["pressureShellIn"]=self.CalibratedReadings["pressure1"]
        self.LabelledReadings["pressureShellOut"]=self.CalibratedReadings["pressure2"]

        self.LabelledReadings["flowRateTube"]=self.CalibratedReadings["flowRate0"]
        self.LabelledReadings["flowRateShell"]=self.CalibratedReadings["flowRate1"]       

    def __init__(self, comport) -> None:


        self.LabelledReadings = {
            "tempTubeIn": 0,
            "tempTubeOut": 0,

            "tempShellIn": 0,
            "tempShell1": 0,
            "tempShell2": 0,
            "tempShell3": 0,
            "tempShell4": 0,
            "tempShellOut": 0,

            "pressureTubeIn": 0,
            "pressureTubeOut": 0,
            "pressureShellIn": 0,
            "pressureShellOut": 0,

            "flowRateTube": 0,
            "flowRateShell": 0
        }   

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

        self.CalibratedReadings = {
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
        print(f'{self.CalibratedReadings["temp0"]}, {self.CalibratedReadings["temp1"]}, {self.CalibratedReadings["temp2"]}, {self.CalibratedReadings["temp3"]}, {self.CalibratedReadings["temp4"]}, {self.CalibratedReadings["temp5"]}, {self.CalibratedReadings["temp6"]}, {self.CalibratedReadings["temp7"]}')

        print('----- Pressure Sensors (KPa) -----')
        print(
            f'{self.CalibratedReadings["pressure0"]}, {self.CalibratedReadings["pressure1"]}, {self.CalibratedReadings["pressure2"]}, {self.CalibratedReadings["pressure3"]}')

        print('----- Flow Sensors (LPM) -----')
        print(
            f'{self.CalibratedReadings["flowRate0"]}, {self.CalibratedReadings["flowRate1"]}')



 


    def printLabeledReadings(self):

        print('----- Sensor Readings -----')

        print('----- Temperature Sensors (Centigrade) -----')
        print(f' Tube In: {self.LabelledReadings["tempTubeIn"]}')
        print(f' Tube Out: {self.LabelledReadings["tempTubeOut"]}')

        print(f' Shell In: {self.LabelledReadings["tempShellIn"]}')
        print(f' Shell 1: {self.LabelledReadings["tempShell1"]}')
        print(f' Shell 2: {self.LabelledReadings["tempShell2"]}')
        print(f' Shell 3: {self.LabelledReadings["tempShell3"]}')
        print(f' Shell 4: {self.LabelledReadings["tempShell4"]}')
        print(f' Shell Out: {self.LabelledReadings["tempShellOut"]}')

        print('----- Pressure Sensors (KPa) -----')
        print(f' Tube In: {self.LabelledReadings["pressureTubeIn"]}')
        print(f' Tube Out: {self.LabelledReadings["pressureTubeOut"]}')

        print(f' Shell In: {self.LabelledReadings["pressureShellIn"]}')
        print(f' Shell Out: {self.LabelledReadings["pressureShellOut"]}')

        print('----- Flow Sensors (LPM) -----')
        print(f'Tube Out: {self.LabelledReadings["flowRateTube"]}')
        print(f'Shell Out: {self.LabelledReadings["flowRateShell"]}')
        
    
        
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
        return self.CalibratedReadings
