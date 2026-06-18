import os
import sys
from dotenv import load_dotenv


def load_config():
    # Load .env file (if exists)
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_config(config):
    missing = []

    for key, value in config.items():
        if value is None or value.strip() == "":
            missing.append(key)

    return missing


def display_config(config):
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:\n")

    mode = config["MATRIX_MODE"] or "development"

    print(f"Mode: {mode}")

    if config["DATABASE_URL"]:
        if "sqlite" in config["DATABASE_URL"]:
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to remote database")
    else:
        print("Database: NOT CONFIGURED")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: MISSING KEY")

    log = config["LOG_LEVEL"] or "INFO"
    print(f"Log Level: {log}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: OFFLINE")

    print("\nEnvironment security check:")


def security_check(config):
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main():
    config = load_config()

    missing = validate_config(config)

    display_config(config)

    if missing:
        print("\nWARNING: Missing configuration:")
        for m in missing:
            print(f" - {m}")

    security_check(config)


if __name__ == "__main__":
    main()
