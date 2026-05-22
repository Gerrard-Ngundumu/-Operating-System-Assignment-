def display_gantt_chart(processes):
    print("\nGantt Chart\n")

    for process in processes:
        print(f"| P{process} ", end="")

    print("|")

process_list = [1, 2, 3, 4]

display_gantt_chart(process_list)