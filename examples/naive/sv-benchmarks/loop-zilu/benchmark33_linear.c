int main() {
  int x = __VERIFIER_nondet_int();
  
  if (!(x>=0)) return 0;
  while (x<100 && x>=0) {
    x++;
  }
//@ assert x>=100;
  return 0;
}