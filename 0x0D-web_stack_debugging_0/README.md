# Web Stack Debugging Project

## Overview
This project is part of a series focusing on web stack debugging. The goal is to debug a Docker container running Apache to ensure it returns a page containing "Hello Holberton" when queried at the root.

## Prerequisites
- Ubuntu 14.04 LTS
- Docker installed

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/alx-system_engineering-devops.git
```

2. Navigate to the project directory:
```bash
cd alx-system_engineering-devops/0x0D-web_stack_debugging_0
```

3. Ensure your Docker environment is set up correctly.

## Usage
1. Run the provided script `0-give_me_a_page`:
```bash
./0-give_me_a_page
```

2. Follow the on-screen instructions to debug and fix the Apache configuration inside the Docker container.

3. Verify functionality by curling the container's port 8080:
```bash
curl 0:8080
```

4. If successful, the response should contain "Hello Holberton."

## Troubleshooting
- If the Apache server fails to start or returns errors, ensure that Docker is running correctly and that there are no conflicts with port mappings.
- Check the Apache configuration files inside the Docker container for any misconfigurations.

## Credits
This project is part of the ALX Software Engineering curriculum, specifically focusing on web stack debugging.

## Author
Refiloe Radebe (_kweenDev_)
