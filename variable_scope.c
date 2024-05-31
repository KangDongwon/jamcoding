#include <stdio.h>
#include <stlib.h>

int i = 0;

void func1()
{
  i = 10;
  printf("%d\n", i);
}

void func2()
{
  int i = 0;
  printf("%d\n", i);
  printf("%d", j); //ERROR
}

void main()
{
  int j = 0;
  
  printf("%d\n", i);
  
  func1();
  
  printf("%d\n", i);
  
  func2();
  
  printf("%d\n", i);
}
