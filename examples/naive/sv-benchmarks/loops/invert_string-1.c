int main() {
    int MAX = __VERIFIER_nondet_uint();
    if(!(MAX > 0)) {abort();}
    char str1[MAX], str2[MAX];
    int cont, i, j;
    cont = 0;
    
    for (i=0; i<MAX; i++) {
        str1[i]=__VERIFIER_nondet_char();
    }
	str1[MAX-1]= '\0';

    j = 0;
    
    for (i = MAX - 1; i >= 0; i--) {
        str2[j] = str1[0];
        j++;
    }

    j = MAX-1;
    for (i=0; i<MAX; i++) {
//@ assert str1[i] == str2[j];
	  j--;
    }
}