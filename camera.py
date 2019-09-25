#from picamera import PiCamera
import threading
from typing import Dict
import datetime
import time
import operator
from PhotoReq import PhotoReq

#Look into better data structure. Ordered set? Hash map? Set queue? 
request_list = []
#id_set = set() #Maybe create set to store ids that have been used. 
                #Check before adding to request_list
complete_list = []

#Look into async library / separate thread for capture.
def capture(request: PhotoReq) -> None:
    '''Capture an image using the raspberry pi camera. Will not work unless picamera module installed.'''

    '''camera = PiCamera()

        try:
            camera.start_preview()
            camera.capture(f'home/pi/Desktop/image_{photo_id}.jpg')
    
        finally:
            camera.stop_preview()
            camera.close()
    '''
    
    request._is_complete = True
    complete_list.append(request)

    write_txt(request._id, is_photo= True)

    
    
                    

def read_input() -> None: 
    '''
    Opens the to_python.txt file. To be executed every second.
    '''
    file = open("to_python.txt", "r")
    contents = file.read()
    contents.strip()
    #check for invalid data : try/ except ?? what do in except
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
        file.write(f"{photo_id}, {photo_id}.jpg")
        print(f"Recorded {photo_id}.jpg")
    file.close()

def try_capture() -> None:
    '''Checks if a picture should be taken, every second'''
    if len(request_list) > 0:
        for request in request_list:
            if not request._is_complete:
                if request._date <= datetime.datetime.now():
                    capture(request)
                    break


def build_photo_request(photo_id: str, time: str, camera_id: str):
    #look into library and clearify timezone issues?
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

    #better name
    photo_time = datetime.datetime(year, month, day, hour, minute, second)

    #Ensure photo id and camera id are > 0. Look into unsigned ints.
    photo_req = PhotoReq(int(photo_id), photo_time, int(camera_id), False)
    
    #This should be its own method.
    
    #Check if object already exists in request list.
    if len(request_list) == 0:
        request_list.append(photo_req)
    else:
        if all(request._id != photo_req._id for request in request_list):
            request_list.append(photo_req)

        for request in request_list:
            #Make a predicate function and call it in first pass of request_list
            if not(request._date == photo_req._date \
                and request._camera_id == photo_req._camera_id) and request._id == photo_req._id :
                
                request_list.remove(request)
                request_list.append(photo_req)
                
            else:
                pass
    
    request_list.sort(key=operator.attrgetter('_date'))
    
    
def timer_callback():
    read_input()
    time.sleep(1)
    try_capture()
    threading.Timer(1.0, timer_callback).start()

timer_callback()