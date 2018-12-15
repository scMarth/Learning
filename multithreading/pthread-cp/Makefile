CC=gcc
CFLAGS=-pthread
DEPS = pthread-cp.h
OBJ = pthread-cp.o pthread-cp-faster.o no-thread.o
EXEC = pthread-cp pthread-cp-faster no-thread

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

all: $(EXEC)

no-thread: no-thread.o
	$(CC) -o $@ $^ $(CFLAGS)

pthread-cp: pthread-cp.o
	$(CC) -o $@ $^ $(CFLAGS)

pthread-cp-faster: pthread-cp-faster.o
	$(CC) -o $@ $^ $(CFLAGS)

clean:
	rm $(OBJ)

spotless:
	rm $(OBJ) $(EXEC)



# gcc -pthread -o pthread-cp pthread-cp.c