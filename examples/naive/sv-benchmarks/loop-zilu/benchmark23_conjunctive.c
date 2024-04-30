int main() {
  int i = __VERIFIER_nondet_int();
  int j = __VERIFIER_nondet_int();
  
  if (!(i==0 && j==0)) return 0;
  while (i<100) {
    j+=2;
    i++;
  }
//@ assert j==200;
  return 0;
}