void func(int k, int j, int n) {  
  if (!(n>=1 && k>=n && j==0)) return ;
  // @ loop invariant j <= n - 1;
  while (j<=n-1) { j++; k--; }
  assert(k>=0);
}