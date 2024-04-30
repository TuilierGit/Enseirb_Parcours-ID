int main()
{
  int x=__VERIFIER_nondet_int();
  int y=__VERIFIER_nondet_int();

  if (y>0)
  {
    while(x<100) 
    {
      x=x+y;
     }
  }                           
//@ assert y<=0 || (y<0 && x>=100);

  return 0;
}