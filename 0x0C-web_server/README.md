# Web Server Configuration Project
### 0x0C-web_server

## Overview

This project focuses on configuring a web server using Bash scripts and Puppet manifests. It covers tasks such as transferring files, installing Nginx, setting up domain names, handling redirections, and customizing error pages.

## Project Structure

The project is divided into several tasks:

1. **Transfer a File to Your Server**
   - Write a Bash script to transfer files using `scp`.
   
2. **Install Nginx Web Server**
   - Bash script to install and configure Nginx on an Ubuntu machine.
   
3. **Setup a Domain Name**
   - Register a domain name and configure DNS records.
   
4. **Redirection**
   - Configure Nginx for URL redirection using a 301 redirect.
   
5. **Not Found Page 404**
   - Customize Nginx's 404 error page.
   
6. **Install Nginx Web Server (w/ Puppet)**
   - Use Puppet for automating Nginx installation and configuration.

## File Structure

The project includes the following files:

- `0-transfer_file`: Bash script for file transfer.
- `1-install_nginx_web_server`: Bash script for Nginx installation.
- `2-setup_a_domain_name`: Domain name configuration.
- `3-redirection`: Bash script for URL redirection in Nginx.
- `4-not_found_page_404`: Bash script for custom 404 page.
- `7-puppet_install_nginx_web_server.pp`: Puppet manifest for Nginx installation.

## Usage

1. Clone the repository.
2. Navigate to task directories.
3. Run scripts or apply Puppet manifests.
4. Follow task-specific instructions.

## Requirements

- OS: Ubuntu 16.04 LTS
- Editors: vi, vim, emacs
- Bash Scripting: Scripts must be executable and Shellcheck compliant.
- Puppet: Manifests must configure Nginx as per tasks.

## Notes

- Update placeholders (e.g., IP addresses, domain names) with actual values.
- Test scripts/configurations in a safe environment before production.

## Author
Refiloe Radebe __(kweenDev)__
