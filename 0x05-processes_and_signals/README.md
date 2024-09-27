# 0x05. Process and signals
#### Processes and Signals Project

## Introduction
This project is a collection of Bash scripts and a C program designed to demonstrate various concepts related to processes, signals, and process management in Unix-like systems.

## File Structure
- **0-what-is-my-pid**: Bash script to display its own PID.
- **1-list_your_processes**: Bash script to display a list of currently running processes.
- **2-show_your_bash_pid**: Bash script to display lines containing the word "bash" and get the PID of the Bash process.
- **3-show_your_bash_pid_made_easy**: Bash script to display the PID and process name of processes containing the word "bash".
- **4-to_infinity_and_beyond**: Bash script to display "To infinity and beyond" indefinitely.
- **5-dont_stop_me_now**: Bash script to stop the 4-to_infinity_and_beyond process.
- **6-stop_me_if_you_can**: Bash script to stop the 4-to_infinity_and_beyond process without using kill or killall.
- **7-highlander**: Bash script to display "To infinity and beyond" indefinitely and react to SIGTERM signal.
- **8-beheaded_process**: Bash script to kill the 7-highlander process.
- **100-process_and_pid_file**: Advanced Bash script that creates a PID file, displays messages, and handles signals.
- **101-manage_my_process**: Advanced Bash script to manage the manage_my_process script.
- **102-zombie.c**: C program to create zombie processes.

## How to Use
1. Clone the repository to your local machine.
2. Navigate to the `0x05-processes_and_signals` directory.
3. Each script or program has a specific purpose and usage as described in its respective section above. Use the provided commands in a terminal to execute each script or program.
4. Follow the instructions and observe the outputs to understand the concepts of processes, signals, and process management.

## Requirements
- Allowed editors: vi, vim, emacs
- All files are interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- All Bash scripts must be executable
- Shellcheck (version 0.7.0 via apt-get) should be used to check for errors
- First line of Bash scripts should be `#!/usr/bin/env bash`
- Second line of Bash scripts should be a comment explaining what the script does

## Notes
- For advanced tasks, additional knowledge about system-level commands and process management in Unix-like systems is required.
- Ensure proper permissions are set for executing Bash scripts and compiling C programs.
- The C program `102-zombie.c` should be compiled using `gcc`.

## Author
This project was created by kweenDev on 2024-04-03.
