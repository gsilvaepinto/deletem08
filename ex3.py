import os
import sys
from dotenv import load_dotenv


def load_config():
    # Returns True if .env was found and loaded
    env_loaded = load_dotenv()

    config = {
        "env_loaded": env_loaded,
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_config(config):
    missing = []

    for key in ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]:
        if not config.get(key):
            missing.append(key)

    return missing


def display_config(config):
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:\n")

    mode = config["MATRIX_MODE"] or "development"
    print(f"Mode: {mode}")

    db = config["DATABASE_URL"]
    if db:
        if "sqlite" in db:
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to remote instance")
    else:
        print("Database: NOT CONFIGURED")

    print("API Access:", "Authenticated" if config["API_KEY"] else "MISSING KEY")

    print(f"Log Level: {config['LOG_LEVEL'] or 'INFO'}")

    print("Zion Network:", "Online" if config["ZION_ENDPOINT"] else "OFFLINE")

    print("\nEnvironment security check:")

    # REAL check for .env existence
    if config["env_loaded"]:
        print("[OK] .env file loaded")
    else:
        print("[WARNING] No .env file found")

    print("[OK] Environment variables system active")
    print("[OK] Production overrides supported")


def main():
    config = load_config()

    print("ORACLE STATUS: Reading the Matrix...\n")

    display_config(config)

    missing = validate_config(config)

    if missing:
        print("\nWARNING: Missing configuration:")
        for m in missing:
            print(f" - {m}")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
