#define a (2)
extern unsigned int __VERIFIER_nondet_uint();
int main() { 
  int i, j=10, n=__VERIFIER_nondet_uint(), sn=0;
  if (n==2147483647) {
    return 0;
  }
  for(i=1; i<=n; i++) {
    if (i<j) 
    sn = sn + a;
    j--;
  }
//@ assert sn==((long long) n)*a || sn == 0;
}