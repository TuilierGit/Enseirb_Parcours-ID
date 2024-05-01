run:
	python3 ./src/main.py


save:
	python3 ./src/main.py --no-color > ./data/output.txt


gpt4all:
	./~/Software/GPT-4-all/bin/chat

install:
	chmod +x scripts/*
	. ./scripts/install.sh

uninstall:
	. ./scripts/uninstall.sh

framactest:
	frama-c -wp test/swap.c test/swap1.h

fc:
	frama-c $1