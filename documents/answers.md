## Mistral OpenOrca

### loops-count_up_down-1.c

Question :

```
  Compute a loop invariant for the following program!
  void func(unsigned int n)
  {
  unsigned int x=n, y=0;
  // @ loop invariant [mask];
  while (x>0){
  x--;y--;
  }
  assert(y==n);
  }
```

Answer :

```
  The loop invariant for this program is:
  [mask] = y == n - x.
```

---

        Exemple 1:

==============================

void func(unsigned int n)
{
unsigned int x=n, y=0;
// @ loop invariant [mask];
while (x>0){
x--;y--;
}
assert(y==n);
}

==============================

The loop invariant for this program is:
[mask] = y == n - x.

==============================

        Exemple 2:

==============================

void func() {
unsigned int x = 0, y = 1;
// @ loop invariant [mask]
while (x < 6) { x++; y \*= 2; }
assert(y % 3 != 0);
}

==============================

Loop Invariant: mask = (x == 5 && y % 3 != 0)

==============================

        Exemple 3:

==============================

void func() {
unsigned int x = 0, y = 1;
// @ loop invariant [mask]
while (x < 6) { x++; y \*= 2; }
assert(y % 3 != 0);
}

==============================

Loop Invariant: mask = n - j >= 1 and k + j == n and j != 0

==============================
