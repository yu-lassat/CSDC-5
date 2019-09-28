# TODO (GoLive) Remove all debugging commands ie. print, asserts

# from picamera import PiCamera
import datetime
import operator
import threading
import time

from PhotoReq import PhotoReq
from comms import Comms
from config import Conf
from enums import MessageTypeOut

request_list = []  # TODO Look into better data structure. Queue?


# TODO Look into async library / separate thread for capture.
def capture(request: PhotoReq) -> None:
    """
    Capture an image using the raspberry pi camera. Will not work unless
    picamera module installed.

    :param request:
    :return:
    """

    # camera = PiCamera()
    #
    # try:
    #     camera.start_preview()
    #     camera.capture(f'home/pi/Desktop/image_{photo_id}.jpg')
    #
    # finally:
    #     camera.stop_preview()
    #     camera.close()

    request.is_complete = True

    Comms.write(MessageTypeOut.PhotoTaken, req_id=request.id)


def read_input() -> None:
    """
    Opens the to_python.txt file. To be executed every second.
    :return:
    """
    file = open(Conf.Comm.FILENAME_IN, "r")
    contents = file.read()
    contents.strip()

    try:
        photo_id, time_, camera_index = contents.split(',')
    except Exception:
        print('Invalid input')
        raise ValueError

    file.close()

    build_photo_request(photo_id, time_, camera_index)
    # TODO Get a object back from build_photo_request to use to get photo_id
    Comms.write(MessageTypeOut.ConfirmRequestReceived, req_id=int(photo_id))


def try_capture() -> None:
    """
    Checks if a picture should be taken, every second
    :return:
    """
    if len(request_list) > 0:
        for request in request_list:
            if not request.is_complete:
                if request.date <= datetime.datetime.now():
                    # TODO Remove request from list so head of list is next
                    # picture to be taken at all times
                    capture(request)
                    break


def build_photo_request(photo_id: str, time_: str, camera_id: str):
    # TODO look into library (and clarify timezone issues <UTC Will be used>)
    date, _time = time_.split('T')
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

    photo_time = datetime.datetime(year, month, day, hour, minute, second)

    # Ensure photo id and camera id are > 0
    # TODO Look into unsigned ints.
    if int(photo_id) >= 0 and int(camera_id) >= 0:
        photo_req = PhotoReq(int(photo_id), photo_time, int(camera_id))
        add_req_to_list(photo_req)
    else:
        raise ValueError


def add_req_to_list(photo_req: PhotoReq):
    if len(request_list) == 0:
        request_list.append(photo_req)
    else:
        id_check_counter = 0
        for request in request_list:
            if request.id != photo_req.id:
                id_check_counter += 1
                if id_check_counter == len(request_list):
                    request_list.append(photo_req)
            elif request.same_id_diff_time_or_camera(photo_req):
                request_list.remove(request)
                request_list.append(photo_req)
            else:
                pass
    request_list.sort(key=operator.attrgetter('date'))


# TODO Change name to main and change filename to main
def timer_callback():
    read_input()
    time.sleep(Conf.Main.LOOP_DELAY)
    try_capture()
    threading.Timer(1.0, timer_callback).start()
    # TODO Change to loop instead of using a callback


timer_callback()
