#include <stdio.h>

typedef struct {
    int tid;
    char status[20];
} Thread;

void display_thread(Thread t) {
    printf("Thread ID: %d\n", t.tid);
    printf("Thread Status: %s\n", t.status);
}

int main() {
    Thread t1 = {101, "Active"};

    display_thread(t1);

    return 0;
}