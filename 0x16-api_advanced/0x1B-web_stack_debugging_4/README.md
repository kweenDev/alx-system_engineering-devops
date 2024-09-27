# 0x1B. Web Stack Debugging #4

## Overview

This project focuses on web stack debugging, where we diagnose and fix issues related to server configuration and file handle limits.
It utilises `Puppet` to automate system configurations and resolve issues. You will handle web server optimisation and fix file descriptor limits for a specific user on a Linux system.

### Technologies

- **Ubuntu 14.04 LTS** (All scripts should be compatible with this OS)
- **Nginx** (Web server being debugged)
- **ApacheBench (ab)** (Benchmarking tool)
- **Puppet** (Configuration management tool)

### Prerequisites

Before running the solutions, ensure you have the following installed:

- **Puppet** (v3.4)
- **nginx** (v1.4.6 or above)
- **apache2-utils** (for `ab`)

##### Install Puppet-lint for Syntax Checking

```bash
apt-get install -y ruby
gem install puppet-lint -v 2.1.1
```

## Tasks :page_with_curl:

- **0. Sky is the limit, let's bring that limit higher**

  - [0-the_sky_is_the_limit_not.pp](./0-the_sky_is_the_limit_not.pp): Puppet manifest
    that increases the amount of traffic an Apache web server can effectively handle.

- **1. User limit**
  - [1-user_limit.pp](./1-user_limit.pp): Puppet manifest that changes the operating system
    configuration so that it is possible to login with the user `holberton` and open a file
    without error.
