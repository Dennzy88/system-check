# 🖥️ System Check Utility

A lightweight Python script that collects and displays key system information such as:

- CPU usage
- RAM usage
- Disk space
- Top processes by memory usage

---

## ⚙️ Features

- Live snapshot of current CPU, RAM, and disk usage
- Lists top 5 processes by memory consumption
- Outputs clean and readable system report
- OS-independent (tested on Windows, should work on macOS/Linux)

---

## 📁 File Structure

```
system-check/
│
├── system_check.py     # Main script
├── .gitignore          # Excludes __pycache__ and temp files
├── README.md           # Project overview and usage
```

---

## ▶️ How to Run

1. Make sure you have **Python 3.x** installed  
2. Install the required package:

```bash
pip install psutil
```

3. Run the script:

```bash
python system_check.py
```

---

## 🔐 .gitignore

```gitignore
__pycache__/
*.pyc
```

---

## 🧠 Use Cases

- Monitor resource usage on development machines
- Useful in debugging performance issues
- Can be extended for logging, alerts or dashboards

---

## 🏷️ Topics

`python` `system-monitoring` `performance` `psutil` `utility` `cli-tool`

---

## 🧑‍💻 Author

Created by **Dennzy88** for personal use and system diagnostics practice.
