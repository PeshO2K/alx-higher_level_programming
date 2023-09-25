#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 *
 * Description: function that prints some basic info about Python lists
 *
 * @p: PyObject pointer
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
    if (PyList_Check(p)) {
        Py_ssize_t size = PyList_Size(p);
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
        for (Py_ssize_t i = 0; i < size; i++) {
            PyObject *item = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
    } else {
        printf("  [ERROR] Invalid List Object\n");
    }
}
/**
 * print_python_bytes - prints python bytes
 *
 * Description: prints python bytes
 *
 * @p: PyObject pointer
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
    if (PyBytes_Check(p)) {
        char *s;
        Py_ssize_t size = PyBytes_AsStringAndSize(p, &s, NULL);
        printf("[*] Python bytes\n");
        printf("  Size: %ld\n", size);
        printf("  Trying string: %s\n", s);
        printf("  First %ld bytes: ", size < 10 ? size + 1 : 10);
        for (Py_ssize_t i = 0; i < size + 1 && i < 10; i++)
            printf("%02hhx%s", s[i], i < 9 && i < size ? " " : "\n");
    } else {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}
/**
 * print_python_float - prints some basic info about Python lists
 *
 * Description: function that prints some basic info about Python lists
 *
 * @p: PyObject pointer
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
    if (PyFloat_Check(p)) {
        double value = PyFloat_AsDouble(p);
        printf("[*] Python float\n");
        printf("  Value: %s\n", PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
    } else {
        printf("  [ERROR] Invalid Float Object\n");
    }
}
