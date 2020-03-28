cimport example.cglib as cglib

cdef extern from "example.h":

    double bessel(double x)

    int ex_raise_error(cglib.GError **error)