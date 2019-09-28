from config import Conf
from enums import MessageTypeOut


class Comms:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Comms.__instance is None:
            Comms()
        return Comms.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Comms.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Comms.__instance = self

    def write(self, msg_type: MessageTypeOut, *, req_id: int) -> None:
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


comms = Comms.get_instance()
