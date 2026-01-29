# 🟢 Website Health Checker & Domain Checker Turmax

This repository contains two Python tools for checking websites and domains:

1. **Website Health Checker** – Checks if websites are up, measures response time, and performs DNS resolution.  
2. **Domain Checker Turmax** – Scan and verify multiple domains for availability, status, and response.

Both tools are lightweight, Python-based, and designed to run on **Termux / Linux / Mac**.

---

## 🔹 Features

### Website Health Checker
- ✅ Check if a website is **UP or DOWN**  
- ✅ Measures **response time (latency)**  
- ✅ Performs **DNS resolution**  
- ✅ Works for **multiple websites/domains** at once  
- ✅ Logs **status and errors**  

### Domain Checker Turmax
- ✅ Check multiple domains in one go  
- ✅ Show **HTTP status**  
- ✅ Measures **DNS resolution**  
- ✅ Works with **Termux / Linux / Mac**  

---

## 🔹 Installation / Auto Setup (1 Command)

Copy and paste the following in **Termux / Linux**:

```bash
pkg update -y && pkg upgrade -y && pkg install python git -y && git clone https://github.com/tzalmamun/Domain-checker-Turmax.git && cd Domain-checker-Turmax && python3 -m pip install --break-system-packages -r requirements.txt && python3 domain_checker.py ```

### Demo

Enter one or multiple URLs/domains separated by space, e.g.:

https://google.com https://example.com

Example output for Website Health Checker:

🔍 Checking: https://google.com
✅ DNS OK → google.com resolves to 142.250.x.x
🌐 Status Code : 200
⏱️ Response Time: 120.45 ms
✅ Website is UP and working fine
--------------------------------------------------
Example output for Domain Checker Turmax:

🔍 Checking: example.com
✅ DNS OK → example.com resolves to 93.184.216.34
🌐 Status Code : 200
⏱️ Response Time: 135.67 ms
--------------------------------------------------
