import pynput.mouse
from pynput.mouse import Button, Listener, Controller
import time
import fastf1
import re
import pandas as pd

# Converts the default string output from the database into a float that can be worked with
def convert_time(time: str) -> float:
    arr = time.split(':')
    num = 60.00
    num += float(arr[1])
    return num

def is_rain(session) -> bool:
    if "True" in str(session.weather_data['Rainfall']):
        return True
    else:
        return False

session = fastf1.get_session(2019, "Hockenheim", "Q")
session.load(weather=True)

drivers = pd.unique(session.laps['Driver'])

# for i in range(20):
#     print(str(session.laps.pick_drivers(drivers[i]).pick_fastest()['LapTime']))
#     print(str(session.laps.pick_drivers(drivers[i]).pick_fastest()['LapTime']).__contains__('nan'))

avg_time = 0.0
num = 20
for i in range(20):
    try:
        avg_time += convert_time(re.findall(r'\d{2}\:\d{2}\.\d{3}', str(session.laps.pick_drivers(drivers[i]).pick_fastest()['LapTime']))[0])
    except:
        try:
            avg_time += convert_time(re.findall(r'(01:\d{2})', str(session.laps.pick_drivers(drivers[i]).pick_fastest()['LapTime']))[0] + ".000")
        except:
            num -= 1
            continue

avg_time /= num
print(avg_time)


#################################
### TEST THE is_rain FUNCTION ###
#################################


# print(is_rain(session))

# print(session.laps.pick_drivers("HAM").pick_fastest()['LapTime'])
