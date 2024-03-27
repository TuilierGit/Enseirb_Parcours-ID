install:
	chmod +x scripts/*
	. ./scripts/install.sh

uninstall:
	. ./scripts/uninstall.sh

gpt4all:
	./~/Software/GPT-4-all/bin/chat

gpt:
	python3 ./src/startGPT.py

framactest:
	frama-c -wp test/swap.c test/swap1.h

fc:
	frama-c $1