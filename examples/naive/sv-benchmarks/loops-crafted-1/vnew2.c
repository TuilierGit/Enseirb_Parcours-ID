int main() {
  unsigned int n,i,k,j;
  n = __VERIFIER_nondet_uint();
  if (!(n <= SIZE)) return 0;
  i = j = k = 0;
  while( i < n ) {
    i = i + 3;
    j = j+3;
    k = k+3;
  }
  if(n>0)
//@ assert i==j && j==k && (i%(SIZE+2));
  return 0;
}