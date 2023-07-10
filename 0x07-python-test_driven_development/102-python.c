#include <Python.h>

void print_python_string(PyObject *p) {
  if (!PyString_Check(p)) {
    printf("p is not a valid string\n");
    return;
  }

  char *s = PyString_AsString(p);
  printf("%s\n", s);
}
