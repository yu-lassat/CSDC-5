from config import Conf
from enums import MessageTypeOut


class Comm:
    _instance = None

    @staticmethod
    def write(msg_type: MessageTypeOut, *, req_id: int) -> None:
        file = open(Conf.Comm.FILENAME_IN, "w")
        # TODO Change to accommodated all message types except errors which
        # need the exceptions to be setup first
        if not msg_type == MessageTypeOut.PhotoTaken:
            file.write(f"rec {req_id}")
            print(f"Recorded {req_id}")
        else:
            file.write(f"{req_id}, {req_id}.jpg")
            print(f"Recorded {req_id}.jpg")
        file.close()
        # TODO Add error checking (Must decide what action to take on errors)

    @staticmethod
    def _get_inst():
        """
        Returns a the instance of the class for internal use. If not
        created, it will be created before being returned
        :return: Instance of Comm for internal use
        """
        if Comm._instance is None:
            Comm._instance = Comm()
        return Comm._instance

    def __init__(self):
        pass
