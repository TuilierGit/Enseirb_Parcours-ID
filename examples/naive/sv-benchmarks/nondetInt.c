#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int __VERIFIER_nondet_int() {
    static int initialized = 0;
    
    if (!initialized) {
        srand(time(NULL));
        initialized = 1;
    }

    return rand();
}
