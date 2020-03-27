#include <example.h>
#include <stdio.h>

int
main (void)
{
  double x = 5.0;
  double y = bessel (x);
  printf ("J0(%g) = %.18e\n", x, y);

  GError *error = NULL;

  if (ex_raise_error (&error) < 0)
    {
      g_assert (error != NULL);
      fprintf (stderr, "Error occured: %s\n", error->message);
      g_error_free (error);
    }

  return 0;
}
