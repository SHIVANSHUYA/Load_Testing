# Load Testing with Locust

A lightweight guide for performing ethical and controlled load testing using Locust.

---

# Overview

This project uses Python and Locust to simulate user traffic against a deployed website for:

- Performance benchmarking
- Response-time analysis
- API stability testing
- Concurrency simulation
- Infrastructure stress observation

---

# Tech Stack

- Python 3.x
- Locust
- HTTP-based Load Simulation

---

# Installation

## 1. Clone Project

```bash
git clone <repository-url>
cd <project-folder>
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install locust
```

---

# Project Structure

```txt
project/
│
├── main.py.py
├── README.md
```

---

# Example Locust Script

```python
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "https://your-domain.com"
    wait_time = between(5, 10)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/136.0.0.0 Safari/537.36"
        )
    }

    @task
    def homepage(self):
        self.client.get("/", headers=self.headers)
```

---

# Running Locust

Start Locust:

```bash
locust -f locustfile.py
```

Open browser:

```txt
http://localhost:8089
```

Configure:
- Number of users
- Spawn rate
- Host URL

Then start the test.

---

# Recommended Safe Settings

| Setting | Recommended |
|---|---|
| Users | 1–10 |
| Spawn Rate | 1 |
| Wait Time | 5–10 sec |
| Duration | Short controlled runs |

---

# Common Errors

## 403 Forbidden

Cause:
- Bot protection
- WAF filtering
- Missing browser headers

Fix:
- Add realistic headers
- Lower request frequency

---

## 429 Too Many Requests

Cause:
- Rate limiting triggered

Fix:
- Reduce concurrency
- Increase wait time

---

## ConnectionResetError

Cause:
- Infrastructure closed connection
- Automated traffic detection

Fix:
- Use slower pacing
- Test locally when possible

---

# Local Testing (Recommended)

Instead of testing production directly:

```bash
npm run dev
```

Then set:

```python
host = "http://localhost:3000"
```

Benefits:
- No WAF interference
- Accurate backend metrics
- Safer benchmarking

---

# Legal & Ethical Notice

## Authorized Usage Only

This project is intended ONLY for:
- Applications you own
- Systems you are authorized to test
- Internal development/staging environments

---

## Do NOT Use For

- Unauthorized stress testing
- Distributed denial-of-service (DDoS)
- Flooding third-party websites
- Attacking public infrastructure
- Circumventing security protections

Unauthorized load testing may:
- Violate hosting provider policies
- Lead to IP bans or account suspension
- Cause service disruption
- Result in legal consequences

---

# Best Practices

- Use gradual traffic ramp-up
- Test staging before production
- Monitor logs during testing
- Keep concurrency reasonable
- Respect platform limits
- Benchmark APIs separately when possible

---

# Example Test Workflow

```txt
1. Start local server
2. Configure Locust users
3. Begin with 1–2 users
4. Observe response metrics
5. Gradually increase load
6. Monitor failures/errors
7. Stop immediately if instability occurs
```

---

# Disclaimer

This repository is for educational and performance-testing purposes only.  
Users are responsible for complying with:
- Local laws
- Hosting provider terms
- Security policies
- Ethical testing standards

Use responsibly.

---

# License

MIT License
