//my_python.c
#include <Python.h>

int main(int argc, char *argv[])
{
  Py_SetProgramName(argv[0]);
  Py_Initialize();
  PyRun_SimpleString("print 'Hello Python!'\n");
  Py_Finalize();
  return 0;
}
