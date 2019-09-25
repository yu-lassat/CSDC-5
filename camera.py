#from picamera import PiCamera
import threading
from typing import Dict
import datetime
import time
import operator
from PhotoReq import PhotoReq

request_list = []
complete_list = []

def capture(photo_id: int) -> None:
    '''Capture an image using the raspberry pi camera. Will not work unless picamera module installed.'''

    '''camera = PiCamera()

        try:
            camera.start_preview()
            camera.capture(f'home/pi/Desktop/image_{photo_id}.jpg')
    
        finally:
            camera.stop_preview()
            camera.close()
    '''
    for request in request_list:
        if request._id == photo_id and request._is_complete == False:
            request._is_complete = True

            write_txt(photo_id, is_photo= True)

    
    for request in request_list:
        if request._is_complete == True:
            complete_list.append(request)

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
    if len(request_list) > 0:
        for request in request_list:
            if request._is_complete == False:
                if request._date <= datetime.datetime.now():
                    capture(request._id)
                    break
    else: 
        pass



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

    photo_req = PhotoReq(int(photo_id), date_time, int(camera_id), False)
    #Check if object already exists in request list.
    if len(request_list) == 0:
        request_list.append(photo_req)
    else:
        if all(request._id != photo_req._id for request in request_list):
            request_list.append(photo_req)

        for request in request_list:
            
            if not(request._id == photo_req._id and request._date == photo_req._date \
                and request._camera_id == photo_req._camera_id) and request._id == photo_req._id :
                
                request_list.remove(request)
                request_list.append(photo_req)
                
            elif request._id == photo_req._id and request._date == photo_req._date \
                and request._camera_id == photo_req._camera_id:
                pass
            
            else:
                pass
    
    request_list.sort(key=operator.attrgetter('_date'))
    
    
def main():
    read_txt()
    time.sleep(1)
    try_capture()
    threading.Timer(1.0, main).start()

main()