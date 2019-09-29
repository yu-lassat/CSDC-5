// ---------------------------------------------------------------------------
#ifndef utilsH
#define utilsH
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ---------------------------------------------------------------------------
/*
 * WARN! Caller Responsible mem returned
 * Returns a string joing the two strings passed unless both are NULL or
 * unable to allocate memory, then NULL shall be returned.
 */
char * ConcatenateChars(const char*, const char*);
// ---------------------------------------------------------------------------
#endif
