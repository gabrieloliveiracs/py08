import sys
import os
import site

curr_py = sys.executable


def not_in_venv() -> None:
    print(f"""MATRIX STATUS: You're still plugged in,\n
    Current Python: {curr_py}
    Virtual Environment: None detected,\n
    WARNING: You're in the global environment!
    The machines can see everything you install.\n
    To enter the construct, run:
    python -m venv matrix_env
    source matrix_env/bin/activate # On Unix
    matrix_env\\Scripts\\activate # On Windows\n
    Then run this program again.""")
    return None


def in_venv() -> None:
    venv_name = os.path.basename(sys.prefix)
    print(f"""MATRIX STATUS: Welcome to the construct\n
    Current Python: {curr_py}
    Virtual Environment: {venv_name}\n
    Environment Path: {sys.prefix}\n
    SUCCESS: You're in an isolated environment!
    Safe to install packages without affecting
    the global system.\n
    Package installation path:
    {site.getsitepackages()[0]}""")


def main() -> None:
    if (sys.prefix == sys.base_prefix):
        return (not_in_venv())
    return (in_venv())


if __name__ == "__main__":
    main()
