cdef extern from "glib.h":

    ctypedef char         gchar;
    ctypedef int          gint;
    ctypedef unsigned int guint32;
    ctypedef guint32      GQuark;

    cdef struct GError_s:
        GQuark domain;
        gint   code;
        gchar *message;

    ctypedef GError_s GError;

    void g_error_free(GError *error)