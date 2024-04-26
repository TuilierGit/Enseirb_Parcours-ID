/*@ ensures A: n >= 1;
  @ ensures B: k >= n - j + 1;
  @ ensures C: j <= n - 1;
  @ assigns k, j, n;
  @ */
void func(int k, int j, int n) {  
  if (!(n>=1 && k>=n && j==0)) return ;
  while (j<=n-1) { j++; k--; }
  assert(k>=0);
}