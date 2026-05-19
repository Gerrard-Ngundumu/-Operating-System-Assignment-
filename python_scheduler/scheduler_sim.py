class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time

def round_robin(processes):
    print("Running Round Robin Scheduling")

    for process in processes:
        print(f"Process {process.pid} executed for {process.burst_time} units")

process_list = [
    Process(1, 4),
    Process(2, 3),
    Process(3, 5)
]

round_robin(process_list)