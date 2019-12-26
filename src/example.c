#include <gsl/gsl_sf_bessel.h>

double bessel(double x)
{
    return gsl_sf_bessel_J0(x);
}
