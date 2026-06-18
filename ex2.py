import importlib
import sys


def check():
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:\n")

    modules = ["pandas", "numpy", "matplotlib"]
    missing = []

    for m in modules:
        try:
            mod = importlib.import_module(m)
            v = getattr(mod, "__version__", "unknown")
            print(f"[OK] {m} ({v})")
        except ImportError:
            print(f"[MISSING] {m}")
            missing.append(m)

    return missing


def main():
    missing = check()

    if missing:
        print("\nMissing dependencies detected.\n")
        print("pip: pip install -r requirements.txt")
        print("poetry: poetry install")
        sys.exit(1)

    print("\nDependency Management Comparison")
    print("pip -> requirements.txt")
    print("poetry -> pyproject.toml\n")

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    data = np.random.randint(0, 100, 1000)
    print("Processing 1000 data points...")

    df = pd.DataFrame({"signal": data})
    print(df.describe())

    plt.hist(df["signal"], bins=30)
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
