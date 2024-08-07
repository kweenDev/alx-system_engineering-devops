# Load balancer
### 0x0F-load_balancer

In this project is a continuation on building up the configuration of the web
server issued in project 0x0B. I was issued with two additional servers, with
one to use for replicating the Nginx configuration of my original server, and
another to set up an HAproxy load balancer, to manage both web servers.

## Tasks :page_with_curl:

* **0. Double the number of webservers**
  * [0-custom_http_response_header](./0-custom_http_response_header): Bash
  script that installs and configures Nginx on a server with a custom HTTP
  response header.
    * The name of the HTTP header is `X-Served-By`.
    * The value of the HTTP header is the hostname of the server.

* **1. Install your load balancer**
  * [1-install_load_balancer](./1-install_load_balancer): Bash script that
  installs and configures HAproxy version 1.5 on a server.
    * Enables management via the init script.
    * Requests are distributed using a round-robin algorithm.

* **2. Add a custom HTTP header with Puppet**
  * [2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp): Similar script to 0-custom_http_response_header that installs and configures Nginx on a server but with Puppet.
    * The name of the custom HTTP header is `X-Served-By`.
    * The value of the HTTP header is the hostname of the server.

## Author
Refiloe Radebe (_kweenDev_)
