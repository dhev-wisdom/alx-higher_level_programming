#include <Python.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        printf("Error: Invalid string object\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    Py_UCS4 *data = PyUnicode_AsUCS4Copy(p);

    if (!data) {
        printf("Error: Failed to get string data\n");
        return;
    }

    printf("String length: %zd\n", length);
    printf("String content: ");

    for (Py_ssize_t i = 0; i < length; i++) {
        printf("%c", data[i]);
    }

    printf("\n");

    PyMem_Free(data);
}

