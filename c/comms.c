#include "comms.h"
#include "utils.h"

#define FILENAME_PYTHON_DIR "python_root.txt"
#define MAX_PYTHON_DIR_LEN 256
#define FILENAME_IN "from_python.txt"
#define FILENAME_OUT "to_python.txt"

int req_id = 1;
char *python_root = NULL;
char *filename_in = NULL;
char *filename_out = NULL;

char* GetPythonRootDir() {
    if (python_root == NULL) {
        FILE *f;
        f = fopen(FILENAME_PYTHON_DIR, "r");
        if (f != NULL) {
            char temp[MAX_PYTHON_DIR_LEN] = "";
            fgets(temp, MAX_PYTHON_DIR_LEN, f);
            fclose(f);

            // Called to allocate mem to keep value when temp goes out of scope
            python_root = ConcatenateChars(temp, NULL);
        }
        else {
            printf("Failed to open file '%s'", FILENAME_PYTHON_DIR);
            python_root = "";
            /* TODO 3 -cError Handling : Add Error handling if unable to open file */
        }
    }
    return python_root;
}

char* GetInputFilename() {
    if (filename_in == NULL) {
        filename_in = ConcatenateChars(GetPythonRootDir(), FILENAME_IN);
    }
    return filename_in;
}

char * GetOutputFilename() {
    if (filename_out == NULL) {
        filename_out = ConcatenateChars(GetPythonRootDir(), FILENAME_OUT);
    }
    return filename_out;
}

void CommsWrite(char *msg) {
    req_id++;
    printf("\nReq ID: %d\n", req_id);

    FILE *f;
    f = fopen(GetOutputFilename(), "w");
    if (!f) {
        printf("Failed to open file");
        return;
    }
    /* TODO 3 -cError Handling : Add Error handling if unable to open file */
    fprintf(f, "%s", msg);
    fclose(f);
    printf("You entered: %s\n", msg);
}

void CommsFree() {
    free(python_root);
    python_root = NULL;

    free(filename_in);
    filename_in = NULL;

    free(filename_out);
    filename_out = NULL;
}
