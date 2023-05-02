
from SensorsReader import SensorsReader
import csv
from datetime import datetime


fieldnames = [
    "timestamp",

    "tempTubeIn",
    "tempTubeOut",

    "tempShellIn",
    "tempShell1",
    "tempShell2",
    "tempShell3",
    "tempShell4",
    "tempShellOut",

    "pressureTubeIn",
    "pressureTubeOut",
    "pressureShellIn",
    "pressureShellOut",

    "flowRateTube",
    "flowRateShell"
]

if __name__ == '__main__':
    sensorsReader = SensorsReader('COM3')
    i = 0


    while (1):
        if (sensorsReader.read()):
            sensorsReader.convertRawReading()
            sensorsReader.LabelReading()
            sensorsReader.printLabeledReadings()
            print(f"----------------{i}----------------")
            i = i+1

            with open('readings.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                if f.tell() == 0:
                    writer.writeheader()
                sensorsReader.LabelledReadings["timestamp"] = datetime.now()
                writer.writerow(sensorsReader.LabelledReadings)

