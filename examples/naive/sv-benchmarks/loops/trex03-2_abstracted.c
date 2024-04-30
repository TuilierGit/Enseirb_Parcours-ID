int main()
{
  unsigned int x1=__VERIFIER_nondet_uint(), x2=__VERIFIER_nondet_uint(), x3=__VERIFIER_nondet_uint();
  unsigned int d1=1, d2=1, d3=1;
  _Bool c1=__VERIFIER_nondet_bool(), c2=__VERIFIER_nondet_bool();
  
  // START HAVOCABSTRACTION
  if ((x3 > (0)) & ((x2 > (0)) & (x1 > (0)))) {
  x3 = __VERIFIER_nondet_uint();
  x2 = __VERIFIER_nondet_uint();
  x1 = __VERIFIER_nondet_uint();
  c2 = __VERIFIER_nondet_bool();
  c1 = __VERIFIER_nondet_bool();
  }
  if ((x3 > (0)) & ((x2 > (0)) & (x1 > (0)))) abort();
  // END HAVOCABSTRACTION

//@ assert x1==0 || x2==0 || x3==0;
  return 0;
}