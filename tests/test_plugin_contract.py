import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "spectrum_analyzer_plugin", ROOT / "__init__.py",
    submodule_search_locations=[str(ROOT)],
)
plugin = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plugin)


def test_plugin_menu_contract():
    info = plugin.get_module_info()
    assert info["name"] == "RTL-SDR Spectrum Analyzer"
    assert info["version"]
    assert callable(plugin.run)


def test_entrypoint_is_lazy():
    # Importing/discovering a plugin must not open SDR hardware or require
    # the runtime dependencies until the user selects Run in the menu.
    assert "scanner" not in plugin.__dict__
