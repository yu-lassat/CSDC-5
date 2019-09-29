/* TODO 4 : Restructure to use a class */
// ---------------------------------------------------------------------------

#ifndef commsH
#define commsH
#include <stdio.h>

// ---------------------------------------------------------------------------
void CommsWrite(char *msg); // Sends msg to python
void CommsFree(); // Frees memory used by comms
// ---------------------------------------------------------------------------
#endif
