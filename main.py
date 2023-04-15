
from SensorsReader import SensorsReader




if __name__ == '__main__':
    sensorsReader=SensorsReader('COM14')
    i=0

    while(1):
        if(sensorsReader.read()):
            sensorsReader.print()
            print(f"----------------{i}----------------")
            i=i+1
            # print(sensorsReader.get()["temp0"])
            # print(sensorsReader.get())
        