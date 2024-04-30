int main() {
  int j = __VERIFIER_nondet_int();
  int k = __VERIFIER_nondet_int();
  int n = __VERIFIER_nondet_int();
  if (!((j==0) && (k==n) && (n>0))) return 0;
  while (j<n && n>0) {
    j++;k--;
  }
//@ assert (k == 0);
  return 0;
}