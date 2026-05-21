#include <stdio.h>
#include <string.h>

void send_message(char message[]) {
    printf("Sending message: %s\n", message);
}

void receive_message(char message[]) {
    printf("Received message: %s\n", message);
}

int main() {
    char msg[] = "Hello from Process A";

    send_message(msg);
    receive_message(msg);

    return 0;
}