#include "utils.h"

char * ConcatenateChars(const char *str1, const char *str2) {
    // Based on https://stackoverflow.com/questions/36437461/safe-way-to-concat-two-strings-in-c
    /* TODO 4 -cTesting : Test method for NULL parameters */
    char *result = NULL;
    size_t n = 0;

    if (str1)
        n += strlen(str1);
    if (str2)
        n += strlen(str2);

    if ((str1 || str2) && (result = malloc(n + 1)) != NULL) {
        *result = '\0';

        if (str1)
            strcpy(result, str1);
        if (str2)
            strcat(result, str2);
    }

    return result;
}
