install:
	chmod +x scripts/*
	. ./scripts/install.sh

uninstall:
	. ./scripts/uninstall.sh

gpt:
	python3 ./src/startGPT.py

framactest:
	frama-c -wp test/swap.c test/swap1.h

fc:
	frama-c $1