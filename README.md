# SpectrumSnek RTL-SDR Analyzer Plugin

Standalone addon for the current SpectrumSnek plugin menu.

## Install and launch

Install through **Utilities → Installed Plugins**, or from the SpectrumSnek root:

```bash
./plugin_manager.sh install analyzer
```

The plugin is installed as `plugins/analyzer`. The menu discovers its `__init__.py` plugin contract (`MODULE_INFO`, `get_module_info()`, and no-argument `run()`) and launches it from the Installed Plugins menu.

The analyzer imports SpectrumSnek's core `sdr_manager.py` at runtime to coordinate exclusive RTL-SDR access with other features. Install it into the SpectrumSnek `plugins/` directory; running the source repository by itself is not a supported standalone mode.

## Features

- Live spectrum display and tuning
- AM/FM/SSB/CW demodulation support
- CTCSS tone detection
- Interactive terminal interface on a capable local terminal
- Web interface automatically selected for SSH or `TERM=dumb` sessions

An RTL-SDR compatible receiver is required for live operation. Hardware-backed testing must be performed on the target device.

## Network access

The web interface listens on all network interfaces so it can be opened from another device. It has no built-in authentication; run it only on a trusted network and restrict access to TCP port 5000 with your firewall.