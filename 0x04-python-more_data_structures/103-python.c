#include <Python.h>

void print_python_list(PyObject *p) {
    long int size, alloc, i;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}

void print_python_bytes(PyObject *p) {
    long int size;
    int i;
    char *trying_str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    trying_str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", trying_str);

    if (size < 10) {
        printf("  first %ld bytes:", size + 1);
    } else {
        printf("  first 10 bytes:");
        size = 9;
    }

    for (i = 0; i <= size; i++) {
        printf(" %02hhx", trying_str[i]);
    }
    printf("\n");
}
