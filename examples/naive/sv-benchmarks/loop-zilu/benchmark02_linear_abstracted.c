int main() {
  int n = __VERIFIER_nondet_int();
  int i = __VERIFIER_nondet_int();
  int l = __VERIFIER_nondet_int();
  i = l;
  if (!(l>0)) return 0;
  // START HAVOCABSTRACTION
  if (i < n) {
  i = __VERIFIER_nondet_int();
  }
  if (i < n) abort();
  // END HAVOCABSTRACTION
//@ assert l>=1;
  return 0;
}