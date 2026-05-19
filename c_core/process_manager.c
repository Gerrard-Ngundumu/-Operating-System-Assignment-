#include <stdio.h>

typedef struct {
    int pid;
    char state[20];
} Process;

void display_process(Process p) {
    printf("Process ID: %d\n", p.pid);
    printf("Process State: %s\n", p.state);
}

int main() {
    Process p1 = {1, "Running"};

    display_process(p1);

    return 0;
}