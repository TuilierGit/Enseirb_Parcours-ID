int main() {
  int i = __VERIFIER_nondet_int();
  int k = __VERIFIER_nondet_int();
  if (!(0 <= k && k <= 1 && i == 1)) return 0;
  while (__VERIFIER_nondet_bool()) {
    i = i + 1;
    k = k - 1;
  }
//@ assert 1 <= i + k && i + k <= 2 && i >= 1;
  return 0;
}