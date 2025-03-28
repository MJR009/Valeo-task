import subprocess

subprocess.run(["python3", "f_cam.py"])
subprocess.run(["python3", "sensor.py"])
subprocess.run(["python3", "resim.py", "f_cam_out.csv", "sensor_out.csv"])
