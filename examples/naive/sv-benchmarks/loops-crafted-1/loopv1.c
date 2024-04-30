int main() {
  int n,i,j;
  n = __VERIFIER_nondet_int();
  if (!(n <= SIZE)) return 0;
  i = 0; j=0;
  while(i<n){ 
 
    if(__VERIFIER_nondet_int())	  
      i = i + 6; 
    else
     i = i + 3;    
  }
//@ assert (i%3) == 0;
  return 0;
}