#define N 1024

int main(void) {
  int A[N];
  int i;

  for (i = 0; i < N; i++) {
    A[i] = __VERIFIER_nondet_int();
  }

  for (i = 0; i < N && A[i] != 0; i++) {
  }

//@ assert i <= N / 2;
}