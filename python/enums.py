from enum import Enum, auto


class MessageTypeOut(Enum):
    ConfirmRequestReceived = auto()
    ErrorAddingRequest = auto()
    ErrorParsingRequest = auto()
    # TODO Change management of errors to use a base exception type with err#
    PhotoTaken = auto()
    PhotoCaptureFailed = auto()
