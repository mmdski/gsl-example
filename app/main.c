#include <stdio.h>
#include <example.h>

int main(void)
{
    double x = 5.0;
    double y = bessel(x);
    printf("J0(%g) = %.18e\n", x, y);
    return 0;
}
