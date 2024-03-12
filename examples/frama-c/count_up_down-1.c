#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

void func(unsigned int n)
{
  unsigned int x=n, y=0;
  // @ loop invariant [mask];
  while (x>0){
    x--;y--;
  }
  assert(y==n);
}