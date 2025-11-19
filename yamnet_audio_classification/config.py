"""
Configuration file for audio detection system
"""
import os

# Audio Configuration
AUDIO_SAMPLE_RATE = 16000  # YAMNet requires 16kHz
AUDIO_CHUNK_SIZE = 16000   # 1 second of audio at 16kHz
AUDIO_CHANNELS = 1         # Mono audio
AUDIO_FORMAT = 'int16'     # 16-bit audio

# I2S Microphone Configuration (INMP441)
# Set to None to auto-detect, or specify device name/index
I2S_DEVICE_NAME = None  # e.g., "seeed-2mic-voicecard" or None for auto-detect
USE_I2S = True  # Set to False to use USB microphone via PyAudio

# GPIO Configuration
LED_PIN = 18

# Detection Configuration
SUSPICIOUS_KEYWORDS = [
    "crying, sobbing",
    "screaming",
    "shout",
    "gunshot",
    "explosion"
]

DETECTION_THRESHOLD = 0.3  # Minimum confidence score to trigger alert

# Alert Configuration
ENABLE_LED_ALERT = True
ENABLE_SOUND_ALERT = True
LED_ALERT_DURATION = 5  # Duration in seconds to keep LED on after detection

# File Paths
LOG_FILE = "audio_detection_log.txt"
ALARM_SOUND_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "alarm.WAV")
YAMNET_MODEL_PATH = os.path.join(os.path.dirname(__file__), "yamnet_model")
CLASS_MAP_PATH = os.path.join(os.path.dirname(__file__), "yamnet_model", "assets", "yamnet_class_map.csv")

# Visualization
ENABLE_PLOT = True  # Set to False to disable real-time plotting

