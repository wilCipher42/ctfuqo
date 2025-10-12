CC=gcc
CFLAGS=-O0 -static

all: challenge

challenge: challenge.c
	$(CC) $(CFLAGS) -o challenge challenge.c
	strip challenge

clean:
	rm -f challenge

.PHONY: all clean
