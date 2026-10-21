"""SpectrumSnek RTL-SDR spectrum analyzer addon."""

__version__ = "1.0.0"
MODULE_INFO = {
    "name": "RTL-SDR Spectrum Analyzer",
    "description": "Real-time RTL-SDR spectrum analysis and analog demodulation.",
    "version": __version__,
    "author": "SpectrumSnek",
    "capabilities": [
        "Real-time spectrum analysis", "AM/FM/SSB/CW demodulation",
        "CTCSS tone detection", "Curses and text interfaces",
    ],
}

def get_module_info():
    return MODULE_INFO

def run():
    from .scanner import main
    main()
