# 0x0E. Web stack debugging #1
### Web Stack Debugging #1

This project focuses on debugging issues related to the web stack, specifically dealing with Nginx configurations to ensure it listens on port 80 as required.

## Task Summaries

### Task #0: Nginx likes port 80

In this task, the goal is to identify and fix the issue causing Nginx not to listen on port 80. The steps involve diagnosing potential conflicts with other processes using port 80 and modifying the Nginx configuration file (`nginx.conf`) to include the necessary `listen 80;` directive. Finally, the Nginx service is restarted to apply the configuration changes.

### Task #1: Make it sweet and short

Task #1 builds upon Task #0 but requires creating a Bash script that accomplishes the fix in a concise manner, limited to 5 lines. The script uses `sed` to modify the Nginx configuration file and then restarts the Nginx service to ensure it listens on port 80 as expected.

## Project Structure

- **0-nginx_likes_port_80:** Bash script for Task #0, which diagnoses and fixes Nginx not listening on port 80.
- **1-debugging_made_short:** Bash script for Task #1, achieving the same fix but in a shorter form.

## Usage

1. Clone the repository to your local machine.
2. Navigate to the appropriate directory (`0x0E-web_stack_debugging_1`).
3. Ensure the Bash scripts are executable (`chmod +x script_name.sh`).
4. Run the scripts to fix the Nginx port 80 issue.

_This project was completed as part of the ALX Africa Software Engineering program by Refiloe Radebe._
