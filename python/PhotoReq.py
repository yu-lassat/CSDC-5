import datetime


class PhotoReq:
    def __init__(self, id_: int, date: datetime.datetime, camera_id: int):
        self.id = id_
        self.date = date
        self.camera_id = camera_id
        self.is_complete = False

    def __eq__(self, other):
        return self.id == other.id and self.date == other.date \
               and self.camera_id == other.camera_id and self.is_complete \
               == other.is_complete

    def same_id_diff_time_or_camera(self, other):
        return (not (self.date == other.date
                     and self.camera_id == other.camera_id) and self.id
                == other.id)
