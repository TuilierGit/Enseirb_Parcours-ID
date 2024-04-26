/*@ ensures A: x == 5 && y == 1 || x == 4 && y == 2 || x == 3 && y == 4 || x == 2 && y == 8 || x == 1 && y == 16;
  @ */
void func() {
  unsigned int x = 0, y = 1;
  // @ loop invariant [mask]
  while (x < 6) { x++; y *= 2; }
  assert(y % 3 != 0);
}
