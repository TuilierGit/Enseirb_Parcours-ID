install:
	. ./scripts/install.sh

gpt:
	python3 ./src/startGPT.py

fc:
	frama-c $1