#!/usr/bin/env python3
"""
Render environment initialization script
Ensures necessary directories and files exist
"""

import os
import sys
from pathlib import Path

def create_directories():
    """Create necessary directories"""
    directories = [
        "data",
        "logs",
        "app/static",
        "app/templates"
    ]

    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")

def check_environment():
    """Check environment variables"""
    required_env_vars = [
        "API_KEYS",
        "ALLOWED_TOKENS"
    ]

    missing_vars = []
    for var in required_env_vars:
        if not os.getenv(var):
            missing_vars.append(var)

    if missing_vars:
        print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
        print("Please set these environment variables in Render console")
        return False

    print("✓ Environment variables check passed")
    return True

def main():
    """Main function"""
    print("🚀 Initializing Render environment...")

    # Create directories
    create_directories()

    # Check environment variables
    if not check_environment():
        sys.exit(1)

    print("✅ Render environment initialization completed!")

if __name__ == "__main__":
    main()
