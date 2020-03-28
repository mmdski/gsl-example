#  cython : language_level=3

cimport cpython.string as pystring

cimport example.cexample as cexample
cimport example.cglib as cglib

def bessel(x):
    return cexample.bessel(x)

def error():

    cdef cglib.GError *error = NULL
    cdef int res
    res = cexample.ex_raise_error(&error)

    if res < 0:
        error_message = (<object> error.message).decode('UTF-8')
        print(error_message)
        cglib.g_error_free(error)