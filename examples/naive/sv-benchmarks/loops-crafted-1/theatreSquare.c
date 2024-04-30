int main()
{

    int a=__VERIFIER_nondet_int(), n=__VERIFIER_nondet_int(), m=__VERIFIER_nondet_int();

    int n_stones1, n_stones2=__VERIFIER_nondet_int();

    n_stones1 = n_stones2;

    if((1 <= n) &&
       (1 <= m) &&
       (1 <= a) &&
       (n <= 109) &&
       (m <= 109) &&
       (a <= 109))
    {
        n_stones1 = correct_version(n, m, a);
        n_stones2 = student_version(n, m, a);
    }
//@ assert n_stones1 == n_stones2;
    return 0;
}