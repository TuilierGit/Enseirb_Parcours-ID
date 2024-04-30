int main() {
  int x = __VERIFIER_nondet_int();
  int y = __VERIFIER_nondet_int();
  if (!(x<y)) return 0;
  // START NAIVELOOPABSTRACTION
  if (x < y) {
  x = __VERIFIER_nondet_int();
  if (!(x < y)) abort();
  if (x<y) {
      x=x+1;
    }
  if (x < y) abort();
  }
  // END NAIVELOOPABSTRACTION
//@ assert x==y;
  return 0;
}