import datetime


class PhotoReq:
    def __init__(self, id_: int, datetime_: datetime.datetime, camera_id: int):
        self.id = id_
        self.datetime = datetime_
        self.camera_id = camera_id
        self.is_complete = False

    def __eq__(self, other):
        return self.id == other.id and self.datetime == other.date \
               and self.camera_id == other.camera_id and self.is_complete \
               == other.is_complete

    def same_id_diff_time_or_camera(self, other):
        return (not (self.datetime == other.datetime
                     and self.camera_id == other.camera_id) and self.id
                == other.id)
