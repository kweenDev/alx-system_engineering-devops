# Airbnb Clone - Web Server Setup with Flask, Gunicorn, and Nginx

## 0x1A. Application Server

This project demonstrates how to serve a Python web application (an Airbnb clone) using Flask for the development environment and Gunicorn with Nginx for the production environment. The web application is served through different routes, including dynamic content and an API, all managed behind an Nginx reverse proxy.

---

## Table of Contents

- [Requirements](#requirements)
- [Environment Setup](#environment-setup)
  - [Task 0: Development Environment with Flask](#task-0-development-environment-with-flask)
  - [Task 1: Production Environment with Gunicorn](#task-1-production-environment-with-gunicorn)
  - [Task 2: Reverse Proxy with Nginx](#task-2-reverse-proxy-with-nginx)
  - [Task 3: Dynamic Route - Odd or Even Number](#task-3-dynamic-route---odd-or-even-number)
  - [Task 4: API Setup](#task-4-api-setup)
  - [Testing](#testing)
  - [Troubleshooting](#troubleshooting)

---

## Requirements

- Ubuntu 20.04 LTS (or similar)
- Python 3.x
- Flask
- Gunicorn
- Nginx
- Git

---

## Environment Setup

### Task 0: Development Environment with Flask

#### 1. **SSH into your server**

Use the following command to SSH into your server:

```bash
ssh ubuntu@<server-ip>
```

#### 2. **Install net-tools(optional)**

Net-tools provides the ifconfig command, useful for network debugging.

```bash
sudo apt update
sudo apt install -y net-tools
```

#### 3. **Clone your AirBnB Clone V2 Project**

Clone your repository to the server:

```bash
git clone https://github.com/yourusername/AirBnB_clone_v2.git
cd AirBnB_clone_v2
```

#### 4. **Configure the Flask Application**

Modify `web_flask/0-hello-route.py` to serve a webpage at /airbnb-onepage/ on port 5000.

```python
#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

#### 5. **Run Flask**

Run the Flask app on your server:

```bash
python3 -m web_flask.0-hello_route
```

#### 6. **Test the Flask app**

In another terminal, run:

```bash
curl http://127.0.0.1:5000/airbnb-onepage/
```

You should see `Hello HBNB!` as the output.

---

### Task 1: Production Environment with Gunicorn

#### 1. **Install Gunicorn**

Gunicorn is a Python WSGI HTTP Server for running web applications.

```bash
sudo apt install python3-pip
pip3 install gunicorn
```

#### 2. **Run the Flask app with Gunicorn**

Use Gunicorn to serve the Flask app on port 5000:

```bash
gunicorn --bind 0.0.0.0:5000
web_flask0.hello_route:app
```

#### 3. **Verify Gunicorn is running**

```bash
curl http://127.0.0.1:5000/airbnb-onepage/
```

You should see the same `Hello HBNB!` message as with Flask.

---

### Task 2: Reverse Proxy with Nginx

#### 1. **Install Nginx**

Install Nginx to act as a reverse proxy for the Gunicorn server:

```bash
sudo apt install -y nginx
```

#### 2. **Configure Nginx**

Open the Nginx configuration file:

```bash
sudo nano /etc/nginx/sites-available/default
```

Modify it to include the following:

```nginx
server {
    listen 80;

    location /airbnb-onepage/ {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### 3. **Restart Nginx**

After making changes, restart Nginx:

```bash
sudo systemctl restart nginx
```

#### 4. **Test the Nginx configuration**

From your local machine or browser, test the public IP of your server:

```bash
curl http://<your-server-ip>/airbnb-onepage/
```

### Task 3: Dynamic Route - Odd or Even Number

#### 1. **Add a dynamic route**

Modify your Flask app to add a new route /number_odd_or_even/<int:n>:

```python
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        return f"Number: {n} is even"
    else:
        return f"Number: {n} is odd"
```

#### 2. **Run Gunicorn on a different port**

Serve the new route using Gunicorn on port 5001:

```bash
gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app
```

#### 3. **Update the Nginx configuration**

Add a new location block to Nginx for the /airbnb-dynamic/ route:

```nginx
location /airbnb-dynamic/number_odd_or_even/ {
    proxy_pass http://127.0.0.1:5001;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

#### 4. **Restart Nginx**

Restart Nginx after modifying the configuration:

```bash
sudo systemctl restart nginx
```

#### 5. **Test the dynamic route**

Test the new route:

```bash
curl http://<your-server-ip>/airbnb-dynamic/number_odd_or_even/5
```

### Task 4: API Setup

#### 1. **Clone the Airbnb Clone V3 Project**

Clone your API repository:

```bash
git clone https://github.com/yourusername/AirBnB_clone_v3.git
cd AirBnB_clone_v3
```

#### 2. **Run Gunicorn for the API**

Serve the API using Gunicorn on port 5002:

```bash
gunicorn --bind 0.0.0.0:5002 api.v1.app:app
```

#### 3. **Configure Nginx to serve the API**

Add a location block to serve the API through Nginx:

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:5002;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

#### 4. **Restart Nginx**

Restart Nginx to apply the changes:

```bash
sudo systemctl restart nginx
```

#### 5. **Test the API**

Test the API endpoint:

```bash
curl http://<your-server-ip>/api/v1/states
```

## Testing

To test the entire setup, you can use the following curl commands:

- For the static route:

```bash
curl http://<your-server-ip>/airbnb-onepage/
```

- For the dynamic number route:

```bash
curl http://<your-server-ip>/airbnb-dynamic/number_odd_or_even/7
```

- For the API:

```bash
curl http://<your-server-ip>/api/v1/states
```

## Troubleshooting

#### 1. **Gunicorn not starting:**

- Check if the app file and app object names are correctly specified in the Gunicorn command.
- Run Gunicorn in the foreground to see detailed error messages:

```bash
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
```

#### 2. **Nginx 502 Bad Gateway:**

- Ensure Gunicorn is running and serving on the correct port.
- Check Nginx logs for errors:

```bash
sudo tail -f /var/log/nginx/error.log
```

#### 3. **Firewall blocking access:**

- Check if the correct ports (80, 5000, 5001, 5002) are open using `ufw`:

```bash
sudo ufw allow 80
sudo ufw allow 5000
sudo ufw allow 5001
sudo ufw allow 5002
```

## Author

Refiloe Radebe
