### March 2025
### Martin Jabůrek
# Valeo DFC Applied Python Evaluation

### Usage

Run the automated script:

`python3 main.py`

... or run each script one by one:

`python3 f_cam.py <output directory>`

`python3 sensor.py <output directory>`

`python3 resim.py <path to...>f_cam_out.csv <path to...>sensor_out.csv <output directory>`

<b>For portability, the script does not compile into an executable.</b>

### Outputs

Each of the scripts creates their respective CSV file.

### Limitations

- The output directory in `resim.py` <b>must</b> be its last argument
- Large overhead due to conversion of floats to text and back
    * May be useful to unite into one script or transfer via binary data
