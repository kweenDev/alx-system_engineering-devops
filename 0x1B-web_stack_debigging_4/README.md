# Web Stack Debugging #4

This project focuses on debugging web server issues and optimizing server configurations using Puppet manifests.

## Task 0: Sky is the limit, let's bring that limit higher

### Problem Statement
The web server setup featuring Nginx is experiencing a high number of failed requests during benchmarking using ApacheBench.

### Solution
To fix this issue, we need to optimize the Nginx configuration and server settings to handle the load effectively.

### Puppet Manifest
The `0-the_sky_is_the_limit_not.pp` manifest contains the necessary configurations to improve the server's performance and reduce failed requests.

## Task 1: User limit

### Problem Statement
There is an issue with the OS configuration preventing the holberton user from logging in and opening files without encountering errors.

### Solution
We need to adjust the OS configuration to resolve the "Too many open files" error for the holberton user.

### Puppet Manifest
The `1-user_limit.pp` manifest addresses the OS configuration issue to allow seamless login and file access for the holberton user.

## Running the Manifests
To apply the Puppet manifests, use the following commands:
```bash
# Task 0
puppet apply 0-the_sky_is_the_limit_not.pp

# Task 1
puppet apply 1-user_limit.pp
```

## Environment
- All files are interpreted on Ubuntu 14.04 LTS.
- Puppet manifests are validated using puppet-lint version 2.1.1.
- Files are checked with Puppet v3.4.

## Author
Refiloe Radebe (_kweenDev_)
