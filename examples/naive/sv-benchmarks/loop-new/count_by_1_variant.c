int main() {
    int i;
    for (i = 0; i != LARGE_INT; i++) {
//@ assert i <= LARGE_INT;
    }
    return 0;
}