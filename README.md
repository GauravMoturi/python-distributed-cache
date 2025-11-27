# Secure In-Memory Caching Service

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Category](https://img.shields.io/badge/Category-Network%20Security-red.svg)]()

This project is a hands-on implementation of a high-performance, in-memory caching service (similar to Redis) with a primary focus on **network security**. The goal is to design and build a custom client-server protocol where all data transmitted after the initial handshake is encrypted, protecting it from eavesdropping.

## Project Vision & Goals

This project explores the intersection of backend systems and security by focusing on:
1.  **Secure Protocol Design:** Creating a simple, stateful protocol for client-server communication.
2.  **Data Confidentiality:** Ensuring that all cache data (keys and values) is encrypted while in transit.
3.  **Concurrency:** Building a server capable of handling multiple simultaneous client connections reliably.
4.  **Performance:** Using efficient data structures for fast key-value lookups.

## Planned Features & Architecture

### Phase 1: Core Caching & Server Logic
-   [ ] Implement a basic TCP socket server that can listen for and accept client connections.
-   [ ] Use a Python dictionary as the in-memory key-value store.
-   [ ] Implement basic commands: `SET <key> <value>`, `GET <key>`, `DELETE <key>`.

### Phase 2: Secure Communication Protocol
-   [ ] Design a simple, custom protocol format (e.g., `[OP_CODE]|[PAYLOAD_LENGTH]|[ENCRYPTED_PAYLOAD]`).
-   [ ] Utilize the `cryptography` library (specifically Fernet symmetric encryption) to secure the payload.
-   [ ] Implement a secure handshake where the server and client establish a shared secret session key for encryption.

### Phase 3: Concurrent Client Handling
-   [ ] Re-architect the server to use Python's `threading` or `asyncio` library.
-   [ ] Ensure the caching data structure is thread-safe to prevent race conditions when multiple clients perform write operations.

### Phase 4: Authentication & Persistence (Future Goals)
-   [ ] Implement a simple token-based authentication system.
-   [ ] Add functionality to periodically save the in-memory cache to a file on disk.

## Technology Stack
*   **Language:** Python 3
*   **Core Libraries:** `socket`, `threading` (or `asyncio`), `cryptography`

## Current Status
**Ongoing.** Project initialized. The basic non-threaded TCP server and client socket structures are under development.

## How to Run (Instructions to come)
_This section will be updated once the core functionality is stable._
