int main() {
  int low = __VERIFIER_nondet_int();
  int mid = __VERIFIER_nondet_int();
  int high = __VERIFIER_nondet_int();
  if (!(low == 0 && mid >= 1 && high == 2*mid)) return 0;
  while (mid > 0) {
    low = low + 1;
    high = high - 1;
    mid = mid - 1;
  }
//@ assert low == high;
  return 0;
}