# SpectrumSnek RTL-SDR Analyzer Plugin

Standalone addon repository for the SpectrumSnek plugin manager.

## Install

From the SpectrumSnek root directory:

```bash
./plugin_manager.sh install-url https://github.com/nomore1007/spectrumsnek-analyzer
```

The analyzer uses SpectrumSnek's core `sdr_manager.py` to coordinate exclusive RTL-SDR access. Launch it from Utilities → Installed Plugins.

## Features

- Live spectrum display and tuning
- AM/FM/SSB/CW demodulation support
- CTCSS tone detection
- Terminal interface and text fallback

Hardware access and interactive UI require an RTL-SDR compatible receiver and must be tested on the target device.
