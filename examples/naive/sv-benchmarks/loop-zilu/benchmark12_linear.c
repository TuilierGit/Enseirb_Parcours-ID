int main() {
  int x = __VERIFIER_nondet_int();
  int y = __VERIFIER_nondet_int();
  int t = __VERIFIER_nondet_int();
  
  if (!(x!=y && y==t)) return 0;
  while (__VERIFIER_nondet_bool()) {
    if(x>0) y=y+x;
  }
//@ assert y>=t;
  return 0;
}