int main() { 
  SIZE=(__VERIFIER_nondet_uint()/8)+1;

  if (SIZE > 1 && SIZE < MAX) {
    int *a = calloc(SIZE,sizeof(int));
    a[SIZE/2]=3;
//@ assert linear_search(a,SIZE,3);
  }
}