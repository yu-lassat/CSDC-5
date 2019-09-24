#from picamera import PiCamera
import threading
from typing import Dict
import datetime
import time
import operator
from PhotoReq import PhotoReq

#Initialize dictionary of string to list of string. Key is photo id, value is list containing time and camera.

#Replace this with priority queue
request_list = []

def capture(photo_id: int) -> None:
    '''Capture an image using the raspberry pi camera. Will not work unless picamera module installed.'''

    #Initialize Camera
    '''camera = PiCamera()'''

    #Adjust flip of camera if necessary.
    '''camera.vflip = True #Flips vertically
    camera.hflip = True #Flips horizontally'''

    #Save image to file path specified as argument to capture.
    '''camera.capture(f'foo/bar/{photo_id}.jpg')'''
    for request in request_list:
        if request._id == photo_id:
            request_list.remove(request)

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

    build_photo_request(photo_id, time, camera_index)
    write_txt(int(photo_id), False)

    

def write_txt(photo_id: int, is_photo: bool) -> None:
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
    
    if request_list[0]._date <= datetime.datetime.now():
        capture(request_list[0]._id)



def build_photo_request(photo_id: str, time: str, camera_id: str):
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

    date_time = datetime.datetime(year, month, day, hour, minute, second)

    photo_req = PhotoReq(int(photo_id), date_time, int(camera_id))
    #Check if object already exists in request list.
    if not any(x._id == photo_req._id for x in request_list):
        request_list.append(photo_req)
        request_list.sort(key=operator.attrgetter('_date'))
    else:
        pass

def thread_callback():
    read_txt()
    time.sleep(0.5)
    try_capture()
    
if __name__ == "__main__":
    threading.Timer(1.0, thread_callback).start()
    
        





