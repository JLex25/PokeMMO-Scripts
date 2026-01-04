from playsound3 import playsound


# Files
ASSEST_FOLDER = 'assets/'
ALARM_FILE = ASSEST_FOLDER + 'alarm.mp3'


def alarm():
    playsound(ALARM_FILE, block=False)
