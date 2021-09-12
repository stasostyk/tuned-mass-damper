from sense_hat import SenseHat
from datetime import datetime
import json
import time

sense = SenseHat()

data_x = []
data_y = []
data_z = []
while True:
    try:
        time.sleep(0.01)
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        print("[+] gathering data")
        data_x.append(x)
        data_y.append(y)
        data_z.append(z)
    except KeyboardInterrupt:
        with open('data.json', 'w', encoding='utf-8') as f:
            print("saving to json file")
            json.dump([data_x, data_y, data_z], f, ensure_ascii=False, indent=4)

        exit()
