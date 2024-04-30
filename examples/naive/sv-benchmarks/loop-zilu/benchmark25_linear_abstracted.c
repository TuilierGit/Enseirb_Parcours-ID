int main() {
  int x = __VERIFIER_nondet_int();
  if (!(x<0)) return 0;
  // START NAIVELOOPABSTRACTION
  if (x < (10)) {
  x = __VERIFIER_nondet_int();
  if (!(x < (10))) abort();
  if (x<10) {
      x=x+1;
    }
  if (x < (10)) abort();
  }
  // END NAIVELOOPABSTRACTION
//@ assert x==10;
  return 0;
}