int main() {
  unsigned int n,i,k;
  n = __VERIFIER_nondet_uint();
  if (!(n <= SIZE)) return 0;
  i = 0;
  while( i < n ) {
    i = i + 1;
  }
  int j = i;
  while( j < n ) {
    j = j+1;
  }
  k = j;
  while( k < n ) {
    k = k+1;
  }
//@ assert (i+j+k)/3 <= SIZE;
  return 0;
}