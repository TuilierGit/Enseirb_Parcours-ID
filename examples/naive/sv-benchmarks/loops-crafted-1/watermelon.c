int main(){

  unsigned int w=__VERIFIER_nondet_uint();

  int is_divisible1 = true, is_divisible2 = true;

  if(w > 0 && w < 10000000)
  {
    is_divisible1 = correct_version(w);
    is_divisible2 = student_version(w);
//@ assert is_divisible1 == is_divisible2;
  }
  return 0;

}