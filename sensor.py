import sys
import os
import csv
import random

def printUsage():
    print("\033[36mUsage: python3 sensor.py <output directory>\033[39m")

def main():
    OUT = "sensor_out.csv"
    PATH = "./"

    if len(sys.argv) >= 2:
        if os.path.isdir(sys.argv[1]):
            PATH = sys.argv[1] + "/"
        else:
            print("\033[31mErr:\033[39m invalid directory path given")
            printUsage()
            sys.exit(1)

    writeCSV(PATH + OUT)



def writeCSV(path):
    file = open(path, "w")

    csvHandle = csv.writer(file)
    csvHandle.writerow(
        ["Timestamp", "Speed"]
    )

    timestamp = genTimestamp()
    currentTS = next(timestamp)
    speed = genSpeed()

    while currentTS < 160_000_000.0:
        csvHandle.writerow(
            [
                currentTS,
                next(speed) # done every time - "each time the column Timestamp has a new value"
            ]
        )
        currentTS = next(timestamp)

    file.close()

def genTimestamp():
    timestamp = 100_000_000.0
    increment = 200_000.0
    while True:
        yield round(timestamp, 6)
        timestamp += increment + random.uniform(-10_000.0, 10_000.0)

def genSpeed():
    speed = 60.0
    increment = 0.56
    while True:
        yield speed
        speed = speed + increment if ( speed < 120.0 ) else 120.0 + random.uniform(-0.1, 0.1)

main()
