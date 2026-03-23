# 🚀 Network Intrusion Detection System (IDS)

A simple Intrusion Detection System built using Python and Scapy to monitor network traffic and detect suspicious activity.

---

## 📌 Features
- Real-time packet sniffing
- Detects high-frequency traffic (possible attack)
- Alerts server when attack detected
- Client-server communication using sockets

---

## 🛠️ Tech Stack
- Python
- Scapy
- Socket Programming

---

## ⚙️ How It Works

1. Agent monitors network traffic
2. Counts packets from each IP
3. If threshold exceeds → attack detected
4. Sends alert to server
5. Server logs alert

---

## ▶️ How to Run

### Step 1: Start Server
```bash
python3 server.py
