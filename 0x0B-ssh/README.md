# 0x0B. SSH

## Overview
This project delves into SSH (Secure Shell) and related topics such as network security, system administration, and DevOps practices. The tasks include creating SSH key pairs, configuring SSH client files, and managing SSH authentication for secure remote access.

## Learning Objectives
By the end of this project, you should understand and be able to explain:
- What is a server and where servers usually live.
- SSH essentials, including creating and using SSH RSA key pairs.
- The advantages of using `#!/usr/bin/env bash` instead of `/bin/bash`.
- How to configure SSH client files for passwordless authentication.
- Using Puppet to automate SSH client configuration.

## Project Structure
- **Tasks**:
  - **Task 0**: Use a private key to connect to a server via SSH.
  - **Task 1**: Create an SSH RSA key pair with specified parameters.
  - **Task 2**: Configure the SSH client file to use a private key and refuse password authentication.
  - **Task 3**: Add an SSH public key to the server for remote access.
  - **Task 4**: Advanced task using Puppet to configure SSH client files for passwordless authentication.

## Resources
- Text and video resources on physical servers, SSH essentials, and SSH configuration.
- References on SSH encryption, connection process, and protocol specifications.

## Requirements
- Editors: vi, vim, emacs.
- Execution on Ubuntu 20.04 LTS.
- All files ending with a new line.
- Mandatory README.md file at the project root.
- Executable Bash scripts with specified shebang (`#!/usr/bin/env bash`).
- Commented Bash scripts explaining script functionality.
- Use of SSH single-character flags.
- No password authentication in SSH configurations.
- SSH configurations using the private key `~/.ssh/school`.

## Project Files
The project includes the following files:
- `0-use_a_private_key`: Bash script for connecting to a server using a private key.
- `1-create_ssh_key_pair`: Bash script for generating an SSH RSA key pair.
- `2-ssh_config`: SSH client configuration file.
- `100-puppet_ssh_config.pp`: Puppet manifest for SSH client configuration automation.
- `README.md`: Project documentation in Markdown format.

## Instructions
Follow the provided tasks and requirements to complete each script and configuration file. Ensure proper file permissions, script execution, and adherence to SSH configuration standards.

---

_This project was completed as part of the ALX Software Engineering program by Refiloe Radebe._
