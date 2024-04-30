int main(void) {
  unsigned int x = 5;
  while (__VERIFIER_nondet_int()) {
    x += 8;
  }
//@ assert (x & 5) == 5;
  return 0;
}