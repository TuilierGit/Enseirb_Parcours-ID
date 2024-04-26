gpt4all:
	./~/Software/GPT-4-all/bin/chat

run:
	python3 ./src/startGPT.py

install:
	chmod +x scripts/*
	. ./scripts/install.sh

uninstall:
	. ./scripts/uninstall.sh

framactest:
	frama-c -wp test/swap.c test/swap1.h

fc:
	frama-c $1