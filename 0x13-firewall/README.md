# 0x13. Firewall

## Introduction

This project focuses on implementing firewall rules using `ufw` (Uncomplicated Firewall) on a Linux server. The goal is to enhance security by blocking all incoming traffic except for specific TCP ports, and to configure port forwarding for specific services.

## Background Context

Firewalls are critical components of network security, acting as barriers between trusted internal networks and potentially malicious external networks. They control incoming and outgoing network traffic based on predetermined security rules.

## Resources

To understand the concepts and tools used in this project, it's recommended to review the following resources:

- [What is a firewall](#) (basic overview of firewall concepts)
- [More Info](#) (additional information on firewall setup and configuration)

## Warning

A cautionary note is provided regarding the potential risks associated with misconfiguring firewall rules, such as inadvertently blocking SSH access or disrupting network services. Proper care must be taken when implementing firewall rules to avoid unintended consequences.

## Tasks

### 0. Block all incoming traffic but

**Objective:**

Configure the `ufw` firewall on the specified server (`web-01`) to block all incoming traffic except for the following TCP ports:

- Port 22 (SSH)
- Port 443 (HTTPS SSL)
- Port 80 (HTTP)

**Implementation:**

The implementation details, including the specific `ufw` commands used to achieve this configuration, are provided in the project repository under the file `0-block_all_incoming_traffic_but`.

### 1. Port forwarding

**Objective:**

Implement port forwarding on the `web-01` server to redirect incoming traffic on port 8080/TCP to port 80/TCP.

**Implementation:**

The configuration changes required to enable port forwarding are documented in the project repository under the file `100-port_forwarding`. This file contains the modified `ufw` configuration settings to facilitate port forwarding.

## Conclusion

By completing these tasks, you'll gain practical experience in firewall management, enhancing your understanding of network security principles and best practices.


## Author
_kweenDev_ (Refiloe Radebe)
