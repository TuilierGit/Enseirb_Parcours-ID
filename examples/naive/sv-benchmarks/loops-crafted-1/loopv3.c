int main() {
  int i,j;
  i = 0; j=0;
  while(i<SIZE){ 

    if(__VERIFIER_nondet_int())	  
      i = i + 8; 
    else
     i = i + 4;    
	  
  }
  j = i/4 ;
//@ assert (j * 4) == i;
  return 0;
}