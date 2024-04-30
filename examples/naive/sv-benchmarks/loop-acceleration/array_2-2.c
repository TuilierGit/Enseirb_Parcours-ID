#define SZ 2048

int main(void) {
  int A[SZ];
  int B[SZ];
  int i;
  int tmp;

  for (i = 0; i < SZ; i++) {
    A[i] = __VERIFIER_nondet_int();
    B[i] = __VERIFIER_nondet_int();
  }

  for (i = 0; i < SZ; i++) {
    tmp = A[i];
    B[i] = tmp;
  }

//@ assert A[SZ/2] == B[SZ/2];
}