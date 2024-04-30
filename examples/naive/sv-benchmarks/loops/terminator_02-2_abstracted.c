int main()
{
    int x=__VERIFIER_nondet_int();
    int z=__VERIFIER_nondet_int();
    if (!(x>-100)) return 0;
    if (!(x<200)) return 0;
    if (!(z>100)) return 0;
    if (!(z<200)) return 0;
    // START HAVOCABSTRACTION
    if ((z > (100)) & (x < (100))) {
    z = __VERIFIER_nondet_int();
    x = __VERIFIER_nondet_int();
    }
    if ((z > (100)) & (x < (100))) abort();
    // END HAVOCABSTRACTION                       

//@ assert x>=100 || z<=100;

    return 0;
}