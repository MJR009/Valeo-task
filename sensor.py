import sys
import os

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

    file.write("test")

    file.close()

# cols - Timestamp, Speed

# timestamp - float [us], start 100s -> 100 000 000us, increment 200ms ->200 000 us +- 10ms -> 10 000us, 6 decimal places
#           - (> 160) s -> 160 000 000 us - stop generating
# speed - float [kmph], start 60 kmph, increment 0.56 kmph every row (<= every new timestamp), when 120 kmph, keep 120 +- 0.1kmph

main()
