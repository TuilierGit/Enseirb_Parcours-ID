#define SZ 2048

int main(void) {
  int A[SZ] = {0};
  int B[SZ] = {0};
  int i;
  int tmp;

  for (i = 0; i < SZ; i++) {
    tmp = A[i];
    B[i] = tmp;
  }

//@ assert A[SZ/2] != B[SZ/2];
}