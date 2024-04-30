int main(void) {
  unsigned int x = 0;
  while (__VERIFIER_nondet_int()) {
    x += 4;
  }
//@ assert !(x % 4);
  return 0;
}