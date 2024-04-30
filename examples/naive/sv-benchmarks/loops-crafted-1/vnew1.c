int main() {
  unsigned int n,i,k;
  n = __VERIFIER_nondet_uint();
  if (!(n <= SIZE)) return 0;
  k = n;
  i = 0;
  while( i < n ) {
    k--;
    i = i + 3;
  }
  int j = 0;
  while( j < n/3 ) {
//@ assert k > 0;
    k--;
    j++;
  }
  return 0;
}