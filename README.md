# High-Performance & Secure Distributed Caching Service

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Category](https://img.shields.io/badge/Category-Backend%20&%20Security-purple.svg)]()

This is an educational project to build a high-performance, in-memory key-value caching service from scratch in Python. The goal is to explore the intersection of **high-performance backend systems** (inspired by Redis) and the **network security principles** required to protect them in a distributed environment.

## Project Vision & Goals

The vision is to create a reliable and fast caching layer suitable for scalable web applications, while ensuring data confidentiality and integrity. The key learning objectives are:
1.  **Concurrency & Performance:** Build a multi-threaded server capable of handling multiple simultaneous client connections without data corruption, using thread-safe data structures for fast read/write operations.
2.  **Network Security:** Design and implement a simple, encrypted client-server protocol to protect all data in transit from eavesdropping.
3.  **Protocol Design:** Implement a robust, text-based command protocol for client-server interaction (e.g., SET, GET, DELETE).
4.  **Low-Level Networking:** Master server and client communication using Python's `socket` library.

## Planned Features & Architecture

The service is being built incrementally in distinct phases:

### Phase 1: Core Single-Client Server
-   [x] **Status: Complete**
-   [x] Implement a basic TCP socket server to handle a single client.
-   [x] Use a Python dictionary as the in-memory store for basic `SET`, `GET`, and `DELETE` commands.

### Phase 2: Concurrent & Thread-Safe Architecture
-   [ ] **Status: In Progress**
-   [ ] Re-architect the server to spawn a new thread for each client connection.
-   [ ] Implement a `threading.Lock` to ensure the core dictionary is thread-safe, preventing race conditions.

### Phase 3: Secure Protocol Implementation
-   [ ] **Status: Planned**
-   [ ] Integrate the `cryptography` library (Fernet) for symmetric encryption.
-   [ ] Implement a secure handshake where the server and client establish a shared session key.
-   [ ] Encrypt all command payloads after the handshake.

### Phase 4: Advanced Features (Future Goals)
-   [ ] Add key expiry (Time-To-Live, TTL) functionality.
-   [ ] Implement basic data persistence to save the cache state to a file.

## Technology Stack
*   **Language:** Python 3
*   **Core Libraries:** `socket`, `threading`, `cryptography`

## Current Status
**Ongoing.** The foundational single-client server is functional. Development is currently focused on implementing the multi-threaded architecture to handle concurrent clients safely. The security layer is the next major planned feature.

## How to Run
1.  Clone the repository and install dependencies: `pip install -r requirements.txt`
2.  Open two separate terminal windows.
3.  In the first terminal, start the server: `python server.py`
4.  In the second terminal, run the client: `python client.py`
