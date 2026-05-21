#include <stdio.h>

void start_system() {
    printf("Operating System Simulation Started\n");
}

void stop_system() {
    printf("Operating System Simulation Stopped\n");
}

int main() {
    start_system();

    printf("Running core modules...\n");

    stop_system();

    return 0;
}