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


def test_remote_or_limited_terminal_uses_live_text_output():
    import ast
    import os
    import sys
    from argparse import Namespace

    source = (ROOT / "scanner.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    helper_node = next(
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "should_use_text_mode"
    )
    namespace = {"os": os, "sys": sys}
    exec(compile(ast.Module(body=[helper_node], type_ignores=[]), "<analyzer-helper>", "exec"), namespace)
    should_use_text = namespace["should_use_text_mode"]

    assert should_use_text(
        Namespace(web=False, text=False),
        environ={"SSH_TTY": "/dev/pts/1", "TERM": "xterm"},
        stdin_isatty=True, stdout_isatty=True,
    )
    assert should_use_text(
        Namespace(web=False, text=False),
        environ={"TERM": "dumb"},
        stdin_isatty=True, stdout_isatty=True,
    )
    assert should_use_text(
        Namespace(web=False, text=True),
        environ={"TERM": "xterm"},
        stdin_isatty=True, stdout_isatty=True,
    )
    assert not should_use_text(
        Namespace(web=True, text=False),
        environ={"SSH_TTY": "/dev/pts/1", "TERM": "dumb"},
        stdin_isatty=True, stdout_isatty=True,
    )
