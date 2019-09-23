#from picamera import PiCamera
import threading
from typing import Dict
import datetime
import time

#Initialize dictionary of string to list of string. Key is photo id, value is list containing time and camera.

#Replace this with priority queue
photo_dict = Dict[str, str]
photo_dict = {}

def capture(photo_id: str) -> None:
    '''Capture an image using the raspberry pi camera. Will not work unless picamera module installed.'''

    #Initialize Camera
    '''camera = PiCamera()'''

    #Adjust flip of camera if necessary.
    '''camera.vflip = True #Flips vertically
    camera.hflip = True #Flips horizontally'''

    #Save image to file path specified as argument to capture.
    '''camera.capture(f'foo/bar/{photo_id}.jpg')'''
    print("In capture")
    photo_dict.__delitem__(photo_id)
    write_txt(photo_id, is_photo= True)


def read_txt() -> None:
    '''
    Opens the to_python.txt file and adds the contents to photo_dict. To be executed every second.
    '''
    file = open("to_python.txt", "r")
    contents = file.read()
    contents.strip()
    photo_id, time, camera_index = contents.split(',')
    file.close()

    if photo_id not in photo_dict:
        photo_dict[photo_id] = [time, camera_index]
        #confirm photo_id
        write_txt(photo_id, is_photo= False)
        
    
    else:
        pass

    

def write_txt(photo_id: str, is_photo: bool) -> None:
    file = open('from_python.txt','w')
    if not is_photo:
        file.write(f"rec {photo_id}")
        print(f"Recorded {photo_id}")
    else:
        file.seek(0)
        file.write(f"{photo_id}, {photo_id}.jpg")
        file.truncate()
        print(f"Recorded {photo_id}.jpg")
    file.close()

def try_capture() -> None:
    '''Checks if a picture should be taken every second'''
    #Replace this for loop with priority queue[0]
    key_counter = 0
    for value in photo_dict.values():
        time = value[0]

        date, _time = time.split('T')
        date.strip()
        _time.strip()
        date = date.split('-')
        _time = _time.split(':')
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        hour = int(_time[0])
        minute = int(_time[1])
        second = int(_time[2].split('.')[0])
       
        if datetime.datetime(year, month, day, hour, minute, second) <= datetime.datetime.now():
            capture(list(photo_dict.keys())[key_counter])
            break
        key_counter += 1


if __name__ == "__main__":
    threading.Timer(1.0, read_txt).start()
    time.sleep(2)
    threading.Timer(1.0, try_capture).start()
        





