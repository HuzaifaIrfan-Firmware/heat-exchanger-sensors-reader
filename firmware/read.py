from time import sleep
from pySerialTransfer import pySerialTransfer as txfer


class struct(object):
    temp0=0
    temp1=0
    temp2=0
    temp3=0

    temp4=0
    temp5=0
    temp6=0
    temp7=0

    analog0=0
    analog1=0
    analog2=0
    analog3=0

    interruptRate0=0
    interruptRate1=0




def printStruct():

    print('----- Sensor Raw Readings -----')

    print('----- Temperature Sensors (Centigrade) -----')
    print(f'{testStruct.temp0}, {testStruct.temp1}, {testStruct.temp2}, {testStruct.temp3}, {testStruct.temp4}, {testStruct.temp5}, {testStruct.temp6}, {testStruct.temp7}')

    print('----- Pressure Sensors (10 bit Analog Read) -----')
    print(f'{testStruct.analog0}, {testStruct.analog1}, {testStruct.analog2}, {testStruct.analog3}')

    print('----- Flow Sensors (Interrupts Per Seconds) -----')
    print(f'{testStruct.interruptRate0}, {testStruct.interruptRate1}')




if __name__ == '__main__':
    try:
        testStruct = struct
        link = txfer.SerialTransfer('COM14')
        
        link.open()
        sleep(5)
    
        while True:
            if link.available():
                recSize = 0
                
                testStruct.temp0 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.temp1 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.temp2 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.temp3 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.temp4 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.temp5 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.temp6 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.temp7 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.analog0 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.analog1 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.analog2 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.analog3 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.interruptRate0 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']

                testStruct.interruptRate1 = link.rx_obj(obj_type='f', start_pos=recSize)
                recSize += txfer.STRUCT_FORMAT_LENGTHS['f']


                printStruct()
                

                
            elif link.status < 0:
                if link.status == txfer.CRC_ERROR:
                    print('ERROR: CRC_ERROR')
                elif link.status == txfer.PAYLOAD_ERROR:
                    print('ERROR: PAYLOAD_ERROR')
                elif link.status == txfer.STOP_BYTE_ERROR:
                    print('ERROR: STOP_BYTE_ERROR')
                else:
                    print('ERROR: {}'.format(link.status))
                
        
    except KeyboardInterrupt:
        link.close()