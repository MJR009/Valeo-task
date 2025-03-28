import sys
import os

# ARGS - f_cam_out.csv, sensor_out.csv

def printUsage():
    print("\033[36mUsage: python3 resim.py <output directory>\033[39m")

def main():
    OUT = "resim_out.csv"
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

    file.write("test")

    file.close()


# cols - Timestamp, FrameID, Speed, YawRate, Signal1, Signal2

# all but Speed from f_cam_out.py
# speed - avarage of the two inputs
#       - take time from f_cam and get closest speed in sensor in the past, take an avarage

main()
