int main() {  
  k = __VERIFIER_nondet_int();
  
  i = 0;
  while(x[i] != 0){
    y[i] = x[i];
    i++;
  }
  y[i] = 0;
  
  if(k >= 0 && k < i)
    if(y[k] != 0)
//@ assert 0;

  return 0;
}