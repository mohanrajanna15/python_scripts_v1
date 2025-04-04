import platform
import sys
import os

def main():
    print("🐍 Python Version:")
    print(f"{sys.version}\n")

    print("💻 OS Version:")
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.architecture()[0]}")

    # Optional: Print environment info
    print("\n🧪 Environment Info:")
    print(f"User: {os.getenv('USER') or os.getenv('USERNAME')}")
    print(f"Home: {os.path.expanduser('~')}")

if __name__ == "__main__":
    main()

