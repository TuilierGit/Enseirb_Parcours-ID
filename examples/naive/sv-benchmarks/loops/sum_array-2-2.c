#define LIMIT 1000000

int main()
{
  unsigned int M = __VERIFIER_nondet_uint();
  if (M > LIMIT) {
    return 0;
  }
  int A[M], B[M], C[M];
  unsigned int  i;
  
  for(i=0;i<M;i++) {
    A[i] = __VERIFIER_nondet_int();
    if (!(A[i] <= LIMIT)) return 0;
    if (!(A[i] >= -LIMIT)) return 0;
  }
  
  for(i=0;i<M;i++) {
    B[i] = __VERIFIER_nondet_int();
    if (!(B[i] <= LIMIT)) return 0;
    if (!(B[i] >= -LIMIT)) return 0;
  }

  for(i=0;i<M;i++)
     C[i]=A[i]+B[i];
  
  for(i=0;i<M;i++)
//@ assert C[i]==A[i]+B[i];
}