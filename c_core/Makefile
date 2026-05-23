CC=gcc
CFLAGS=-Wall

all:
	$(CC) $(CFLAGS) process_manager.c -o process_manager
	$(CC) $(CFLAGS) thread_manager.c -o thread_manager
	$(CC) $(CFLAGS) ipc_module.c -o ipc_module
	$(CC) $(CFLAGS) main_sim.c -o main_sim

clean:
	del *.exe