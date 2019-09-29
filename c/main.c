#pragma hdrstop
#pragma argsused

#include <stdio.h>
#include "comms.h"

#ifdef _WIN32
#include <tchar.h>
#else
typedef char _TCHAR;
#define _tmain main
#endif

int _tmain(int argc, _TCHAR* argv[]) {
    /* TODO 2 -cComms : Check incoming file for info */
    /* TODO 3 -cData Structure : Track Pending Requests */
    /* TODO 3 -cData Structure : Track Which Requests Are not confirmed */
    /* TODO 4 -cError Handling : Check if request is pending for too long
     without confirmation */
    /* TODO 2 : Start Python Script */
    /* TODO 4 : Confirm the python program started correctly */
    char received[100] = ""; /* TODO 4 : Remove variable used for testing */
    while (strcmp(received, "exit")) {
        printf("Enter number of seconds to ofset time by: ");
        gets(received);
        /* TODO 1 : Change value into a time offset from now and send to python */
        CommsWrite(received);
    }

    CommsFree();

    return 0;
}
