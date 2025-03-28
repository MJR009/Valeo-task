import sys
import os
import csv
import random

def printUsage():
    print("\033[36mUsage: python3 f_cam.py <output directory>\033[39m")

def main():
    OUT = "f_cam_out.csv"
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
        ["Timestamp", "FrameID", "Speed", "YawRate", "Signal1", "Signal2"]
    )

    timestamp = genTimestamp()
    frameID = genFrameID()
    speed = genSpeed()

    for _ in range(2_000):
        csvHandle.writerow(
            [
                next(timestamp),
                next(frameID),
                next(speed),
                "",
                "",
                ""
            ]
        )

    file.close()

def genFrameID():
    id = 100
    while True:
        yield id
        id += 1

def genTimestamp():
    timestamp = 100_000_000.0
    increment = 27_700.0
    while True:
        yield round(timestamp, 6)
        timestamp += increment + random.uniform(-50.0, 50.0)

def genSpeed():
    speed = 60.0
    increment = 0.08
    while True:
        yield speed
        speed = speed + increment if ( speed < 120.0 ) else 120.0 + random.uniform(-0.05, 0.05)
        # < used, <= (or ==) on float is invalid

# yawrate - float [°/s], start 0, then in range od +- 1 every frame # per each frame? not english
# signal1 - int, 0 up to id 200, for > 200 select random from 1 - 15 and keep constant
# signal2 - signal1 < 5 -> 0; signal1 >= 5 80 +- 10 every frame

main()
