import os

folders = [
    "docs/screenshots",
    "c_core/include",
    "c_core/race_demo",
    "c_core/tests",
    "python_scheduler/outputs",
    "controller",
    "logs",
    "tests"
]

files = [
    "README.md",
    ".gitignore",
    "pcb_snapshot.json",

    "c_core/Makefile",
    "c_core/process_manager.c",
    "c_core/thread_manager.c",
    "c_core/ipc_module.c",
    "c_core/main_sim.c",

    "python_scheduler/scheduler_sim.py",
    "python_scheduler/gantt.py",

    "controller/main_controller.py"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, "w") as f:
        pass

print("Project structure created successfully!")