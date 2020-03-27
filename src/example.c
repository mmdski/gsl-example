#include <example.h>
#include <gsl/gsl_sf_bessel.h>

enum ExExampleError
{
  EX_EXAMPLE_ERROR_OCCURED
};

double
bessel (double x)
{
  return gsl_sf_bessel_J0 (x);
}

#define EX_EXAMPLE_ERROR ex_example_error_quark ()

GQuark
ex_example_error_quark (void)
{
  return g_quark_from_static_string ("ex-example-error-quark");
}

int
ex_raise_error (GError **error)
{
  g_return_val_if_fail (error == NULL || *error == NULL, FALSE);

  if (TRUE)
    {
      g_set_error (error, EX_EXAMPLE_ERROR, EX_EXAMPLE_ERROR_OCCURED,
                   "Example error");
      return -1;
    }
  else
    return 0;
}
