import sys
import os
import csv

def printUsage():
    print("\033[36mUsage: python3 resim.py <path to...>f_cam_out.csv <path to...>sensor_out.csv <output directory>\033[39m")

def printError(message):
    print(message)
    printUsage()
    sys.exit(1)

def checkInputFiles():
    INPUTS = ["f_cam_out.csv", "sensor_out.csv"]
    paths = ["", ""]

    if os.path.isfile(sys.argv[1]):
        fileName = os.path.basename(sys.argv[1])
        if fileName not in INPUTS:
            printError("\033[31mErr:\033[39m argument 1 not a valid file")

        if fileName == "f_cam_out.csv":
            paths[0] = sys.argv[1]
        else:
            paths[1] = sys.argv[1]
        INPUTS.remove(fileName) # remove to not find the same file twice
    else:
        printError("\033[31mErr:\033[39m argument 1 is not a file")

    if os.path.isfile(sys.argv[2]):
        fileName = os.path.basename(sys.argv[2])
        if fileName not in INPUTS:
            printError("\033[31mErr:\033[39m argument 2 not a valid file or reused")

        if fileName == "f_cam_out.csv":
            paths[0] = sys.argv[2]            
        else:
            paths[1] = sys.argv[2]
    else:
        printError("\033[31mErr:\033[39m argument 2 is not a file")

    return paths[0], paths[1] # to later open, we need the paths



def main():
    OUT = "resim_out.csv"
    PATH = "./"
    f_cam_path = ""
    sensor_path = ""

    if len(sys.argv) < 3:
        printError("\033[31mErr:\033[39m not enough command line arguments")
    else:
        f_cam_path, sensor_path = checkInputFiles()
        if len(sys.argv) > 3:
            if os.path.isdir(sys.argv[3]):
                PATH = sys.argv[3] + "/"
            else:
                printError("\033[31mErr:\033[39m invalid directory path given")

    writeCSV(PATH + OUT, f_cam_path, sensor_path)



def writeCSV(out, f_cam, sensor):
    file = open(out, "w")
    f_cam_file = open(f_cam, "r")
    sensor_file = open(sensor, "r")

    csvHandle = csv.writer(file)
    f_cam_Handle = csv.reader(f_cam_file)
    next(f_cam_Handle) # skip header
    sensor_Handle = csv.reader(sensor_file)
    next(sensor_Handle)

    csvHandle.writerow(
        ["Timestamp", "FrameID", "Speed", "YawRate", "Signal1", "Signal2"]
    )

    for row in f_cam_Handle:
        csvHandle.writerow(
            [
                row[0],
                row[1],
                ( float(row[2]) + getClosestSensorSpeed(sensor_Handle, float(row[0])) ) / 2,
                row[3],
                row[4],
                row[5]
            ]
        )

        sensor_file.seek(0)
        sensor_Handle = csv.reader(sensor_file) # go back to start
        next(sensor_Handle)

    sensor_file.close()
    f_cam_file.close()
    file.close()

def getClosestSensorSpeed(sensor_Handle, referenceTimestamp):
    previous = 0

    for row in sensor_Handle:
        timestamp = float(row[0])

        if (timestamp > referenceTimestamp):
            return previous
        
        previous = float(row[1])
        
main()
