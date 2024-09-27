# Web Infrastructure Design

This project focuses on designing various web infrastructures covering simple setups, secured and monitored configurations, and scalable architectures.

## Project Overview

The goal of this project is to create and document different web infrastructure designs, ranging from basic setups to advanced configurations, incorporating security, monitoring, and scalability principles.

## Tasks

### 1. Simple Web Stack

The task involves designing a basic web infrastructure using a single server with a LAMP stack and hosting a website reachable via www.foobar.com.

#### Requirements:
- 1 server
- 1 web server (Nginx)
- 1 application server (PHP)
- 1 database (MySQL)
- Domain name foobar.com with www record pointing to server IP
- Explain server, domain name, DNS record, web server, application server, database, and communication with users.
- Identify issues like SPOF, downtime during maintenance, scalability limitations.

### 2. Secured and Monitored Web Infrastructure

This task focuses on designing a secured and monitored web infrastructure with HTTPS, firewalls, and monitoring clients.

#### Requirements:
- 1 server
- 1 load balancer (HAproxy)
- Split components (web server, application server, database) on separate servers
- 3 firewalls
- SSL certificate for HTTPS
- 3 monitoring clients
- Explain the purpose of each element and the necessity for security and monitoring.
- Discuss issues such as SSL termination, single MySQL server for writes, and uniform server components.

### 3. Scale Up - Web Infrastructure Design

The final task involves designing a scalable web infrastructure with load balancing and split server components.

#### Requirements:
- 1 server for each component (web server, application server, database)
- 1 load balancer (HAproxy) configured as a cluster
- Explain the benefits of split components, load balancing, and HAproxy clustering.
- Discuss issues related to consistency, load balancer overhead, and resource allocation.

## Repository Structure

The project is organized into directories for each task:
- Directory: 0x09-web_infrastructure_design
  - File: 0-simple_web_stack
  - File: 1-distributed_web_infrastructure_design
  - File: 2-secured_and_monitored_web_infrastructure
  - File: 3-scale_up

## Usage

To replicate or understand each web infrastructure design, refer to the respective markdown files for detailed explanations, diagrams, and considerations.

## Contributors

- Refiloe Radebe
