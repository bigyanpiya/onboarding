Onboarding Tasks

The tasks cover topics such as **log aggregation strategies, drift detection, motion detection, model deployment, impersonation controls, and automated reporting**.  

---

## 📂 Project Contents

### 1. `kyraworks.py`
A consolidated Python script demonstrating multiple AI/ML and system tasks:

- **User Impersonation Controls**  
  - Role-based access checks, audit logging, session expiry, and manual termination.

- **Drift Detection for Bandwidth Streams**  
  - **Page-Hinkley Test** – detects abrupt mean changes.  
  - **Windowed KS Test** – detects distributional changes using Kolmogorov-Smirnov statistic.  
  - Visualizes drift detection on simulated bandwidth data.

- **Data Archiving Script**  
  - Archives directories into `.tar.gz` files.  
  - Generates JSON metadata (source, timestamp, archived files).

- **Basic Motion Detection**  
  - Uses OpenCV frame differencing to detect movement between consecutive video frames.

- **Basic Object Detector Training (TensorFlow Lite)**  
  - MobileNetV2-based lightweight model.  
  - Converted to **TFLite** for real-time inference.  
  - Webcam demo with predictions overlayed on frames.

- **Daily Privacy Zone Report Generation**  
  - Creates CSV reports of dummy security events.  
  - Displays logs in a colorful **Rich console table**.  
  - Simulates daily email reporting.

---

### 2. `kyraworks task.pdf`
Documentation of onboarding solutions:

- **Log Aggregation Strategy**  
  - Collect logs from applications, servers, databases, IoT devices, and networks.  
  - Standardize formats (JSON/CSV), secure transport (TLS/SSL).  
  - Store in Elasticsearch, Splunk, AWS S3, or GCP Logging.  
  - Apply preprocessing, anonymization, and real-time alerting.

- **Feedback Data Storage Schema**  
  - Database schema with three tables:  
    - `alerts` – generated alerts.  
    - `users` – system users.  
    - `alert_feedback` – structured feedback linked to alerts and users.  
  - Supports tracking false positives/negatives and retraining triggers.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+  
- Install dependencies:
  ```bash
  pip install numpy matplotlib opencv-python tensorflow rich
