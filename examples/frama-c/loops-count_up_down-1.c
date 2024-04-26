/*@ ensures A: y == n - x;
  @ assigns y, n, x;
  @ */

void func(unsigned int n)
{
  unsigned int x=n, y=0;
  while (x>0){
    x--;y++;
  }
  assert(y==n);
}