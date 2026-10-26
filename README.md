# 🛡️ Cloud-Fortress

A secure and lightweight cloud container project built with Python and Docker, focusing on cloud security best practices and the principle of least privilege.

## 🚀 Project Overview
**Cloud-Fortress** is a micro-cloud environment designed to run a secure Python HTTP server inside an isolated Docker container, ensuring maximum protection against unauthorized privilege escalation.

## 🔒 Security Best Practices Implemented
1. **Non-Root User Execution:** Unlike default Docker containers that run as `root`, this project creates and runs under a dedicated, unprivileged user (`appuser`).
2. **Minimal Attack Surface:** Built on `python:3.9-slim` to reduce image size and eliminate unnecessary system packages.
3. **Explicit Port Mapping & Isolation:** Securely exposes port `8080` while maintaining full container isolation.

## 🛠️ How to Run Locally
1. Build the Docker image:
   ```bash
   docker build -t cloud-fortress .
   
