import sys
import os

def printUsage():
    print("\033[36mUsage: python3 resim.py <path to...>f_cam_out.csv <path to...>sensor_out.csv <output directory>\033[39m")

def printError(message):
    print(message)
    printUsage()
    sys.exit(1)

def checkInputFiles():
    INPUTS = ["f_cam_out.csv", "sensor_out.csv"]

    if os.path.isfile(sys.argv[1]):
        fileName = os.path.basename(sys.argv[1])
        if fileName not in INPUTS:
            printError("\033[31mErr:\033[39m argument 1 not a valid file")
        INPUTS.remove(fileName) # remove to not find the same file twice
    else:
        printError("\033[31mErr:\033[39m argument 1 is not a file")

    if os.path.isfile(sys.argv[2]):
        fileName = os.path.basename(sys.argv[2])
        if fileName not in INPUTS:
            printError("\033[31mErr:\033[39m argument 2 not a valid file or reused")
    else:
        printError("\033[31mErr:\033[39m argument 2 is not a file")



def main():
    OUT = "resim_out.csv"
    PATH = "./"

    if len(sys.argv) < 3:
        printError("\033[31mErr:\033[39m not enough command line arguments")
    else:
        checkInputFiles()
        if len(sys.argv) > 3:
            if os.path.isdir(sys.argv[3]):
                PATH = sys.argv[3] + "/"
            else:
                printError("\033[31mErr:\033[39m invalid directory path given")

    writeCSV(PATH + OUT)



def writeCSV(path):
    file = open(path, "w")

    file.write("test")

    file.close()


# cols - Timestamp, FrameID, Speed, YawRate, Signal1, Signal2

# all but Speed from f_cam_out.py
# speed - avarage of the two inputs
#       - take time from f_cam and get closest speed in sensor in the past, take an avarage

main()
