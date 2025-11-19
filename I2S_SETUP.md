# INMP441 I2S Microphone Setup Guide

This guide will help you set up the INMP441 24-bit I2S omnidirectional microphone on your Raspberry Pi.

## Hardware Connections

Connect the INMP441 to your Raspberry Pi as follows:

| INMP441 Pin | Raspberry Pi Pin | GPIO Number | Description |
|-------------|------------------|-------------|-------------|
| VDD         | Pin 1 (3.3V)     | -           | Power (3.3V) |
| GND         | Pin 6 (GND)      | -           | Ground |
| WS (LRCL)   | Pin 35           | GPIO 19     | Word Select (Left/Right Clock) |
| SCK (BCLK)  | Pin 12           | GPIO 18     | Bit Clock |
| SD          | Pin 38           | GPIO 20     | Serial Data |

**Important:** Make sure to use 3.3V for VDD, not 5V, as the INMP441 is a 3.3V device.

## Software Configuration

### 1. Enable I2S Interface

Edit the Raspberry Pi configuration:

```bash
sudo raspi-config
```

Navigate to:
- **Interface Options** → **I2S** → **Enable**

Alternatively, you can enable I2S by adding this line to `/boot/config.txt`:

```bash
sudo nano /boot/config.txt
```

Add or uncomment:
```
dtparam=i2s=on
```

Reboot your Raspberry Pi:
```bash
sudo reboot
```

### 2. Install Required Packages

The system uses `sounddevice` which interfaces with ALSA. Make sure ALSA utilities are installed:

```bash
sudo apt-get update
sudo apt-get install -y alsa-utils python3-pip
```

### 3. Verify I2S Device

After rebooting, check if the I2S device is recognized:

```bash
arecord -l
```

You should see your I2S device listed. Common names include:
- `seeed-2mic-voicecard`
- `I2S` or similar

You can also check with:

```bash
aplay -l
```

### 4. Test Audio Recording

Test the microphone with:

```bash
arecord -D hw:0,0 -f S16_LE -r 16000 -c 1 test.wav
```

Press Ctrl+C after a few seconds, then play it back:

```bash
aplay test.wav
```

### 5. Configure in the Project

The audio detection system will auto-detect I2S devices. If you need to specify a particular device:

1. Edit `yamnet_audio_classification/config.py`
2. Set `I2S_DEVICE_NAME` to match your device name from `arecord -l`
3. Or leave it as `None` for auto-detection

Example:
```python
I2S_DEVICE_NAME = "seeed-2mic-voicecard"  # If your device has this name
```

## Troubleshooting

### Device Not Found

If the I2S device is not detected:

1. **Check wiring** - Ensure all connections are secure
2. **Verify I2S is enabled** - Check `/boot/config.txt` has `dtparam=i2s=on`
3. **Check device tree overlay** - Some setups require specific overlays in `/boot/config.txt`
4. **Try USB fallback** - Set `USE_I2S = False` in `config.py` to use USB microphone

### No Audio Input

If you get no audio:

1. **Check volume levels:**
   ```bash
   alsamixer
   ```
   Press F6 to select your I2S device, then adjust volume

2. **Test with arecord:**
   ```bash
   arecord -D hw:0,0 -f S16_LE -r 16000 -c 1 -d 5 test.wav
   ```

3. **Check permissions:**
   ```bash
   sudo usermod -a -G audio $USER
   ```
   Then log out and log back in

### Low Quality Audio

For better audio quality:

1. Ensure proper power supply (3.3V, stable)
2. Keep wires short to reduce interference
3. Use proper grounding
4. Check that sample rate matches (16kHz for YAMNet)

## Alternative: Using USB Microphone

If you prefer to use a USB microphone instead:

1. Edit `yamnet_audio_classification/config.py`
2. Set `USE_I2S = False`
3. The system will automatically use PyAudio with USB devices

## Additional Resources

- [Raspberry Pi I2S Documentation](https://www.raspberrypi.org/documentation/configuration/audio-config.md)
- [INMP441 Datasheet](https://www.invensense.com/products/digital/inmp441/)
- [ALSA Documentation](https://www.alsa-project.org/wiki/Documentation)

