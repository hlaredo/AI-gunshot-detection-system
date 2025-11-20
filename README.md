# Raspberry Pi AI Gunshot Detection System

[![GitHub](https://img.shields.io/github/license/hlaredo/AI-gunshot-detection-system)](https://github.com/hlaredo/AI-gunshot-detection-system)
[![GitHub stars](https://img.shields.io/github/stars/hlaredo/AI-gunshot-detection-system)](https://github.com/hlaredo/AI-gunshot-detection-system/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/hlaredo/AI-gunshot-detection-system)](https://github.com/hlaredo/AI-gunshot-detection-system/network)
[![GitHub issues](https://img.shields.io/github/issues/hlaredo/AI-gunshot-detection-system)](https://github.com/hlaredo/AI-gunshot-detection-system/issues)

An AI-powered real-time audio detection system using YAMNet on Raspberry Pi, capable of:

- Detecting **suspicious sounds** (screaming, crying, gunshot, etc.) using Google's YAMNet model
- Supporting **INMP441 24-bit I2S omnidirectional microphone** for high-quality audio capture
- Activating a **warning LED** for 5 seconds when gunshot or suspicious sounds are detected
- Logging events locally for traceability

## 📋 Table of Contents

- [How It Works](#how-it-works)
- [Hardware Setup](#hardware-setup)
- [Installation](#installation)
- [Running the System](#running-the-system)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

---

## How It Works

| Component            | Description |
|----------------------|-------------|
| `audio_detect.py`    | Uses YAMNet for real-time sound classification via I2S/USB microphone |
| `config.py`          | Configuration file for easy customization |
| GPIO (LED)           | Alerts via LED when suspicious sounds detected |
| Log Files            | Events are recorded locally for traceability |

---

## Hardware Setup

- Raspberry Pi (3B+, 4, or 5 recommended)
- **INMP441 24-bit I2S Omnidirectional Microphone** (primary) or USB Microphone (fallback)
- LED + 470 Ohm Resistor (on GPIO pin 21)
- Breadboard + Wires

### INMP441 I2S Microphone Wiring

Connect the INMP441 to your Raspberry Pi:

| INMP441 Pin | Raspberry Pi Pin | Description |
|-------------|------------------|-------------|
| VDD         | 3.3V (Pin 1)     | Power       |
| GND         | GND (Pin 6)      | Ground      |
| WS (LRCL)   | GPIO 19 (Pin 35) | Word Select |
| SCK (BCLK)  | GPIO 18 (Pin 12) | Bit Clock   |
| SD          | GPIO 20 (Pin 38) | Serial Data |

**Important GPIO Pin Assignments:**
- **I2S Microphone:** GPIO 18 (SCK), GPIO 19 (WS), GPIO 20 (SD)
- **LED Alert:** GPIO 21 (Pin 40) - *Changed from GPIO 18 to avoid conflict with I2S*

**Note:** After wiring, you may need to configure the I2S interface in Raspberry Pi OS. The system will attempt to auto-detect the I2S device, or you can configure it manually in `config.py`.

---

## Project Structure

```text
AI-gunshot-detection-system/
├── yamnet_audio_classification/
│ ├── audio_detect.py      # Main detection script
│ ├── config.py            # Configuration file
│ └── yamnet_model/        # YAMNet model files
│     ├── assets/
│     │   └── yamnet_class_map.csv
│     └── saved_model.pb
│
├── assets/
│   └── alarm.WAV          # Alarm sound file (optional)
│
├── media/
│
├── requirements.txt
├── .gitignore
├── I2S_SETUP.md          # I2S microphone setup guide
└── README.md
```
---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/hlaredo/AI-gunshot-detection-system.git
cd AI-gunshot-detection-system
```

2. **Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure I2S Audio (if using INMP441)**
   
   The system will attempt to auto-detect I2S devices. If you need to manually configure:
   - Edit `yamnet_audio_classification/config.py`
   - Set `I2S_DEVICE_NAME` to your specific device name if needed
   - Or set `USE_I2S = False` to use USB microphone instead

---

## Running the System

### Sound Detection (YAMNet)
```bash
cd yamnet_audio_classification
python audio_detect.py
```

The system will:
- Auto-detect and configure audio input (I2S or USB microphone)
- Display available audio devices on startup
- Plot real-time confidence of top 5 sound classes (if enabled)
- Turn on LED for 5 seconds when suspicious sounds are detected
- Log detections to `audio_detection_log.txt`

**Supported Detection Classes:**
- Crying, sobbing
- Screaming
- Shout
- Gunshot
- Explosion

---

## Event Logging
Detection script log alerts to:

- `audio_detection_log.txt`
  
Each log includes a timestamp and detected event.

---

## Customization

All configuration options are in `yamnet_audio_classification/config.py`:

### Detection Settings
```python
SUSPICIOUS_KEYWORDS = [
    "crying, sobbing",
    "screaming",
    "shout",
    "gunshot",
    "explosion"
]

DETECTION_THRESHOLD = 0.3  # Minimum confidence (0.0-1.0)
```

### Alert Settings
```python
ENABLE_LED_ALERT = True      # Enable/disable LED alerts
ENABLE_SOUND_ALERT = True    # Enable/disable sound alerts
LED_ALERT_DURATION = 5       # Duration in seconds to keep LED on after detection
ENABLE_PLOT = True           # Enable/disable real-time plotting
```

### Audio Settings
```python
USE_I2S = True               # Use I2S microphone (INMP441) or USB
I2S_DEVICE_NAME = None       # Auto-detect or specify device name
AUDIO_SAMPLE_RATE = 16000    # YAMNet requires 16kHz
```

### Hardware Settings
```python
LED_PIN = 21                 # GPIO pin for LED (changed from 18 to avoid I2S conflict)
```

---

## 📚 Additional Documentation

- **[I2S Setup Guide](I2S_SETUP.md)** - Detailed instructions for setting up the INMP441 I2S microphone

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🐛 Issues

If you encounter any issues or have suggestions, please [open an issue](https://github.com/hlaredo/AI-gunshot-detection-system/issues) on GitHub.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## Credits

- YAMNet from [Google Research](https://github.com/tensorflow/models/tree/master/research/audioset/yamnet)

  Note: YAMNet model is loaded locally from the `yamnet_model/` directory and downloaded from https://www.kaggle.com/models/google/yamnet.
- Dataset labeling using [Roboflow](https://roboflow.com/)

---
