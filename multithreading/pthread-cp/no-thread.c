#include <stdio.h>
#include <stdlib.h>

volatile long int a = 0;

void func(void)
{
    int i;
    long int localA = 0;

    for(i = 1; i < 500000; i++)
    {
        a = a + i;
    }
}

void func2(void)
{
    int i;
    long int localA = 0;

    for(i = 500000; i <= 1000000; i++)
    {
        a = a + i;
    }
}

int main(int argc, char **argv)
{
    int i;
    a = 0;

    func();
    func2();

    printf("%ld\n", a);
}