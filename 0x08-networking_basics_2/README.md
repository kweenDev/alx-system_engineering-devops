# 0x08. Networking basics #1
#### Networking Basics 2

This repository contains Bash scripts that demonstrate various networking concepts. Below are the details of each script and their functionalities.

## Task 0: Change Your Home IP

### Description
This Bash script configures an Ubuntu server with specific IP configurations:
- It updates the `/etc/hosts` file so that localhost resolves to `127.0.0.2`.
- It updates the `/etc/hosts` file so that `facebook.com` resolves to `8.8.8.8`.

### Usage
1. Make sure you have permissions to execute the script: `chmod +x 0-change_your_home_IP`
2. Run the script with sudo permissions: `sudo ./0-change_your_home_IP`

## Task 1: Show Attached IPs

### Description
This Bash script displays all active IPv4 IPs on the machine it's executed on using the `ifconfig` command.

### Usage
1. Make sure you have permissions to execute the script: `chmod +x 1-show_attached_IPs`
2. Run the script: `./1-show_attached_IPs`

## Task 2: Port Listening on Localhost

### Description
This Bash script listens on port 98 on localhost using the `nc` (netcat) command.

### Usage
1. Make sure you have permissions to execute the script: `chmod +x 100-port_listening_on_localhost`
2. Run the script in one terminal window: `sudo ./100-port_listening_on_localhost`
3. In another terminal window, connect to localhost on port 98 using telnet: `telnet localhost 98`
4. Type some text in the telnet session to send it to the script listening on port 98.

##### Author
kweenDev
##### Date
2024-04-04
