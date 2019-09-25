import datetime

class PhotoReq:
    def __init__(self, id: int, date: datetime.datetime, camera_id: int):
        self._id = id
        self._date = date
        self._camera_id = camera_id
        self._is_complete = False
   
    def __eq__(self, other):
        return self._id == other._id and self._date == other._date \
        and self._camera_id == other._camera_id and self._is_complete == other._is_complete