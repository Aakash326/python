import datetime
import time
from playsound import playsound

def set_alarm():
    alarm_time = input("Set the alarm time (HH:MM:SS, 24-hour format): ")

    # Convert input string to hour, minute, and second
    alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(":"))

    print(f"Alarm set for {alarm_time} ⏰")

    while True:
        # Get current time in HH:MM:SS
        now = datetime.datetime.now().strftime("%H:%M:%S")

        if now == alarm_time:
            print("⏰ Wake up! It's time!")
            playsound("alarm.mp3")  # Make sure this file exists in the same folder
            break

        time.sleep(1)

set_alarm()
