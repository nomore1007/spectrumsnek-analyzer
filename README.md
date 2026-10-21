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

- Live spectrum measurements from an RTL-SDR
- Peak frequency and signal-level output in limited/SSH terminals
- Interactive spectrum display and tuning on a capable local terminal
- AM/FM/SSB/CW demodulation support
- CTCSS tone detection
- Shared SDR ownership through the core `sdr_manager.py`

When curses is unavailable or the terminal is limited, the plugin continuously prints measured peak frequency, FFT level, and median spectrum level. Use Ctrl+C to stop it. The web interface is owned by SpectrumSnek core and is not launched automatically by this plugin.

An RTL-SDR compatible receiver is required for live operation. Hardware-backed testing must be performed on the target device.

The standalone `--web` option remains available for debugging, but normal SpectrumSnek web UI integration belongs in core.
