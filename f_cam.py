import sys
import os

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

    file.write("test")

    file.close()

# cols - Timestamp, FrameID, Speed, YawRate, Signal1, Signal2

# timestamp - float [us], first 100s -> 100 000 000us, inc. 27.7ms -> 27 700us, +-0.05ms -> +- 50us, 6 decimal places
# frameid - icremental id, start 100, end 2100
# speed - float [kmph], start 60, increment 0.08 kmph up to 120, then always 120 +- 0.05 kmph
# yawrate - float [°/s], start 0, then in range od +- 1 every frame # per each frame? not english
# signal1 - int, 0 up to id 200, for > 200 select random from 1 - 15 and keep constant
# signal2 - signal1 < 5 -> 0; signal1 >= 5 80 +- 10 every frame

main()
