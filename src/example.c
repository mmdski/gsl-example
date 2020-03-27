#include <glib.h>
#include <gsl/gsl_sf_bessel.h>

#define EX_EXAMPLE_ERROR ex_example_error_quark ()

enum ExExampleError
{
  EX_EXAMPLE_ERROR_OCCURED
};

GQuark
ex_example_error_quark (void)
{
  return g_quark_from_static_string ("ex-example-error-quark");
}

double
bessel (double x)
{
  return gsl_sf_bessel_J0 (x);
}

gboolean
raise_error (GError **error)
{
  g_return_val_if_fail (error == NULL || *error == NULL, FALSE);

  if (TRUE)
    {
      g_set_error (error, EX_EXAMPLE_ERROR, EX_EXAMPLE_ERROR_OCCURED,
                   "Example error");
      return FALSE;
    }
  else
    return TRUE;
}
