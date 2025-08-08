#!/usr/bin/env python3
"""
ARTH Red Team Terminal Launcher
Simple launcher script for the ARTH AI safety testing tool
"""

import os
import sys
import subprocess

def main():
    """Launch the ARTH Red Team Terminal"""
    print("🚀 Launching ARTH AI Red Team Terminal...")
    
    # Check if arth.py exists
    if not os.path.exists('arth.py'):
        print("❌ Error: arth.py not found in current directory")
        sys.exit(1)
    
    # Check if Python dependencies are available
    try:
        import openai
        import requests
    except ImportError as e:
        print(f"❌ Missing dependencies: {e}")
        print("💡 Install with: pip install -r requirements.txt")
        sys.exit(1)
    
    # Launch the main application
    try:
        subprocess.run([sys.executable, 'arth.py'])
    except KeyboardInterrupt:
        print("\n\n👋 ARTH Red Team Terminal closed.")

if __name__ == "__main__":
    main()