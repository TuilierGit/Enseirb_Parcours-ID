#define N 1024

int main(void) {
  int A[N];
  int i;

  for (i = 0; i < N-1; i++) {
    A[i] = __VERIFIER_nondet_int();
  }

  A[N-1] = 0;

  for (i = 0; A[i] != 0; i++) {
  }

//@ assert i <= N;
}