int main() {
  int x = __VERIFIER_nondet_int();
  int y = __VERIFIER_nondet_int();
  if (!(x < 100 && y < 100)) return 0;
  // START NAIVELOOPABSTRACTION
  if ((y < (100)) & (x < (100))) {
  x = __VERIFIER_nondet_int();
  y = __VERIFIER_nondet_int();
  if (!((y < (100)) & (x < (100)))) abort();
  if (x < 100 && y < 100) {
      x=x+1;
      y=y+1;
    }
  if ((y < (100)) & (x < (100))) abort();
  }
  // END NAIVELOOPABSTRACTION
//@ assert x == 100 || y == 100;
  return 0;
}