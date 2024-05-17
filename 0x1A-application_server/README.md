# 0x1A Application Server

## DevOps and SysAdmin Project

## Concepts Covered
This project focuses on key concepts including:
- Web Servers
- Servers
- Web stack debugging

## Background Context
The project builds upon existing web infrastructure powered by Nginx. The objective is to integrate an application server, link it with Nginx, and enable it to serve content for an Airbnb clone project.

## Requirements Overview
### General
- A README.md file is mandatory at the root of the project folder.
- All Python-related tasks must use python3.
- All configuration files must be properly commented.
### Bash Scripts
- Bash script files should be interpreted on Ubuntu 16.04 LTS.
- Files must end with a new line.
- Bash scripts must be executable.
- Shellcheck must be passed without errors.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.

## Tasks Overview

### 0. Set up development with Python
This task involves setting up the development environment on web-01 to serve content for AirBnB clone v2.

### 1. Set up production with Gunicorn
In this task, the production application server is configured with Gunicorn on web-01, port 5000.

### 2. Serve a page with Nginx
Nginx is configured to serve content from the route /airbnb-onepage/ both locally and on its public IP on port 80.

### 3. Add a route with query parameters
Nginx is configured to proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001.

### 4. Let's do this for your API
The project serves content for AirBnB clone v3 - RESTful API on web-01. Nginx is set up to route /api/ to a Gunicorn instance on port 5002.

### 5. Serve your AirBnB clone
Content from web_dynamic/2-hbnb.py is served by a Gunicorn instance on port 5003, with Nginx configured to serve static assets from web_dynamic/static/.

### 6. Deploy it!
A systemd script is written to start a Gunicorn process serving web_dynamic/2-hbnb.py with 3 worker processes, logging errors in /tmp/airbnb-error.log and access in /tmp/airbnb-access.log.

### 7. No service interruption
A Bash script is created to reload Gunicorn in a graceful way, ensuring minimal downtime during updates.

## GitHub Repository
- Repository: [alx-system_engineering-devops](#)
- Directory: 0x1A-application_server

## Author
Refiloe Radebe (_kweenDev_)
