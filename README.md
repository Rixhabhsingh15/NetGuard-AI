# NetGuard AI – Intelligent Network Fault Detection and Troubleshooting System

An AI-powered network monitoring and fault diagnosis system that combines **Machine Learning, Python, Flask, and GNS3** to identify network issues and provide troubleshooting recommendations.

## Overview

NetGuard AI is designed to monitor network performance, detect abnormal network conditions, classify potential faults, and suggest corrective actions.

The system uses network performance parameters and a Random Forest machine learning model to assist in identifying common network faults.

## Key Features

- **AI-Based Fault Detection:** Uses a Random Forest classifier to identify network fault categories.
- **Live Network Monitoring:** Tracks network connectivity, latency, jitter, and packet loss.
- **PCAP Analysis:** Analyzes packet capture files to assist with network fault diagnosis.
- **Automated Troubleshooting Suggestions:** Provides recommendations based on detected fault categories.
- **Web Dashboard:** Displays monitoring and diagnosis information through a Flask-based interface.
- **Network Simulation:** Uses GNS3 to simulate network topologies and test network conditions.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python |
| Machine Learning | Scikit-learn, Random Forest |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| Network Simulation | GNS3 |
| Network Analysis | PCAP, Traffic Control (tc/netem) |
| Data Processing | Pandas, NumPy |

## System Architecture

1. **Network Simulation:** GNS3 provides a simulated network environment.
2. **Data Collection:** Network monitoring components collect performance metrics.
3. **Fault Prediction:** The Random Forest model classifies network conditions.
4. **PCAP Analysis:** Packet captures can be analyzed for additional diagnostic information.
5. **Troubleshooting:** The system maps detected fault categories to recommendations.
6. **Dashboard:** Flask presents monitoring and diagnosis results through a web interface.

## Fault Categories

The machine learning model is designed to classify the following conditions:

- Normal
- Congestion
- Device Overload
- Link Failure
- Routing Issue

## Project Structure

```text
NetGuard-AI/
│
├── app.py
├── live_monitor.py
├── network_monitor.py
├── train_model.py
├── generate_dataset.py
├── troubleshooting.py
├── pcap_analyzer.py
├── test.py
├── model.pkl
├── dataset.csv
│
├── captures/
│   └── Local packet captures (not included in GitHub)
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Rixhabhsingh15/NetGuard-AI.git
cd NetGuard-AI
```

### 2. Install Dependencies

```bash
pip install flask pandas numpy scikit-learn scapy
```

Install any additional packages required by your local environment.

### 3. Run the Application

```bash
python app.py
```

### 4. Open the Dashboard

Visit:

```text
http://127.0.0.1:5000
```

## Machine Learning

The project uses a Random Forest classifier trained using network performance metrics, including:

- Latency
- Packet Loss
- Jitter
- Bandwidth
- CPU Utilization
- Memory Utilization
- Error Rate

The trained model is stored in `model.pkl`.

## Future Enhancements

- Real-time integration with additional network devices.
- Improved fault prediction using larger real-world datasets.
- Automated network recovery mechanisms.
- Advanced visualization and historical performance analytics.
- Integration with additional network monitoring protocols.

## Project Information

**Project Name:** NetGuard AI – AI-Based Intelligent Network Fault Detection and Troubleshooting System Using Machine Learning

**Domain:** Artificial Intelligence, Machine Learning, Computer Networks

**Institution:** KIIT – Kalinga Institute of Industrial Technology

---

*NetGuard AI aims to make network monitoring smarter, fault diagnosis faster, and troubleshooting more efficient.*
