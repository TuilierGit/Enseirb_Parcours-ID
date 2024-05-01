void func() {
  unsigned int x = 0, y = 1;
  // @ loop invariant [mask]
  while (x < 6) { x++; y *= 2; }
  assert(y % 3 != 0);
}
