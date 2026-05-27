@echo off

echo =====================================
echo RUNNING PYTHON SCHEDULER
echo =====================================

python python_scheduler\scheduler_sim.py

echo.
echo =====================================
echo RUNNING CONTROLLER MODULE
echo =====================================

python controller\main_controller.py

echo.
echo =====================================
echo COMPILING PROCESS MANAGER
echo =====================================

gcc c_core\process_manager.c -o process_manager

echo RUNNING PROCESS MANAGER
process_manager

echo.
echo =====================================
echo COMPILING THREAD MANAGER
echo =====================================

gcc c_core\thread_manager.c -o thread_manager

echo RUNNING THREAD MANAGER
thread_manager

echo.
echo =====================================
echo COMPILING IPC MODULE
echo =====================================

gcc c_core\ipc_module.c -o ipc_module

echo RUNNING IPC MODULE
ipc_module

echo.
echo =====================================
echo COMPILING MAIN SIMULATION
echo =====================================

gcc c_core\main_sim.c -o main_sim

echo RUNNING MAIN SIMULATION
main_sim

echo.
echo =====================================
echo PROJECT EXECUTION FINISHED
echo =====================================

pause