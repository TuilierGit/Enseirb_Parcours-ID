int main()
{
  unsigned int x = 0;
  unsigned int y = 0;
  unsigned int z = 0;
  unsigned int w = 0;

  while (x < 0x0fffffff) {
    y = 0;

    while (y < 0x0fffffff) {
   	z =0;
	// START NAIVELOOPABSTRACTION
	if (z < (268435455)) {
	z = __VERIFIER_nondet_uint();
	if (!(z < (268435455))) abort();
	if (z <0x0fffffff) {
		  z++;
		}
	if (z < (268435455)) abort();
	}
	// END NAIVELOOPABSTRACTION
//@ assert z % 4;
	y++;
    }
//@ assert y % 2;

    x++;
  }
//@ assert x % 2;
  return 0;

}