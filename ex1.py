import sys
import os
import site

in_venv = hasattr(sys, "real_prefix") or sys.base_prefix != sys.prefix

if in_venv:
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    venv_name = os.path.basename(venv_path)

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print()
    print(f"Package installation path: {site.getsitepackages()[0]}")

else:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("    python3 -m venv matrix_env")
    print("    source matrix_env/bin/activate  # On Unix")
    print("    matrix_env\\Scripts\\activate     # On Windows")
    print()
    print("Then run this program again.")
