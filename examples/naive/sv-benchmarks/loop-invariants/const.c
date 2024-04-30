int main(void) {
  unsigned int s = 0;
  while (__VERIFIER_nondet_uint()) {
    if (s != 0) {
      ++s;
    }
    if (__VERIFIER_nondet_uint()) {
//@ assert s == 0;
    }
  }
  return 0;
}