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
