int main() {
  int i = __VERIFIER_nondet_int();
  int j = __VERIFIER_nondet_int();
  int k = __VERIFIER_nondet_int();
  
  if (!(i==0 && j==0)) return 0;
  while (i <= k) {
    i++;
    j=j+1;
  }
//@ assert j==i;
  return 0;
}