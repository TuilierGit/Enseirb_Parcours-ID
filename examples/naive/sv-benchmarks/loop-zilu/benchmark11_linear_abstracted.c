int main() {
  int x = __VERIFIER_nondet_int();
  int n = __VERIFIER_nondet_int();
  
  if (!(x==0 && n>0)) return 0;
  // START NAIVELOOPABSTRACTION
  if (x < n) {
  x = __VERIFIER_nondet_int();
  if (!(x < n)) abort();
  if (x<n) {
      x++;
    }
  if (x < n) abort();
  }
  // END NAIVELOOPABSTRACTION
//@ assert x==n;
  return 0;
}