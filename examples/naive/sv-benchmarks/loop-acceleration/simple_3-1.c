int main(void) {
  unsigned int x = 0;
  unsigned short N = __VERIFIER_nondet_ushort();

  while (x < N) {
    x += 2;
  }

  //@ assert x % 2;
}