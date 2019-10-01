class Conf:
    class Camera:
        PHOTO_LOCATION_AND_PREFIX = 'images/img'
        PHOTO_EXTENSION = '.jpg'
        ENABLED = False
        PHOTO_DELAY = 2

    class Main:
        LOOP_DELAY = 1

    class Comm:
        FILENAME_IN = "to_python.txt"
        FILENAME_OUT = "from_python.txt"
