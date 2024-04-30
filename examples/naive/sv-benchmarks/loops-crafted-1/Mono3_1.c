int main(void) {
  unsigned int x = 0;
  unsigned int y = 0;
  while (x < 1000000) {
    if (x<500000) {
	y++;
    } else {
	y--;
    }
	x++;
  }
//@ assert y!=0) ;;
}