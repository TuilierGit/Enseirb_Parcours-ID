#define LIMIT 1000000

int main() {
    int x=__VERIFIER_nondet_int();
    int y=__VERIFIER_nondet_int();
    if (!(y <= LIMIT)) return 0;

    if (y>0) {
        // START HAVOCABSTRACTION
        if (x < (100)) {
        x = __VERIFIER_nondet_int();
        }
        if (x < (100)) abort();
        // END HAVOCABSTRACTION
    }

//@ assert y<=0 || (y>0 && x>=100);

    return 0;
}