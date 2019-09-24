import datetime

class PhotoReq:
    def __init__(self, id: int, date: datetime.datetime, camera_id: int):
        self._id = id
        self._date = date
        self._camera_id = camera_id