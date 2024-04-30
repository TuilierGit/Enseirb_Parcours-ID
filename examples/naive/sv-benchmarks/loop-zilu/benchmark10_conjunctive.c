int main() {
  int i = __VERIFIER_nondet_int();
  int c = __VERIFIER_nondet_int();
  
  if (!(c==0 && i==0)) return 0;
  while (i<100) {
    c=c+i;
    i=i+1;
    if (i<=0) break;
  }
//@ assert c>=0;
  return 0;
}