# I TOOK HELP FROM CHATGPT TO WRITE THIS README FILE

# rpc-assignment1
# RPC Calculator Assignment (rpc-assignment1)

## Overview

This repository contains an implementation of a basic **Remote Procedure Call (RPC) Calculator Server** and a corresponding **Client**. The server is built using the **Flask** framework, providing two core functionalities: addition (`/add`) and multiplication (`/multiply`).

## Core Components

* **`server-ahsan.py`**: The RPC server application.
* **`client-ahsan.py`**: A standalone client that calls the server endpoints and includes the required **2-second timeout** mechanism.
* **`Dockerfile`**: Defines the environment to containerize the application (ready for deployment).

## How to Run Locally

1.  Install dependencies: `pip3 install -r requirements.txt`
2.  Run the server in one terminal: `python3 server.py`
3.  Run the client in a second terminal: `python3 client.py`

### Testing with cURL (Manual Test)

The running server can be tested manually using the following cURL commands. Ensure the server is running locally via `python3 server.py` before testing.

### 1. Add Operation (`/add`)
```bash
curl -X POST [http://127.0.0.1:8080/add](http://127.0.0.1:8080/add) -H "Content-Type: application/json" -d '{"x": 10, "y": 5}'

### 2. Mutiply Operation (`/multiply`)

curl -X POST [http://127.0.0.1:8080/multiply](http://127.0.0.1:8080/multiply) -H "Content-Type: application/json" -d '{"x": 4, "y": 5}'

## Note on Dockerization (For Sir Yasir)

Due to hardware and operating system limitations (**macOS 12.6.4** does not support current Docker Desktop/Colima versions), the final **Docker Image build and deployment were not possible** on my machine.

The **`Dockerfile`** has been completed as per the requirements, and the local server/client tests pass successfully.
