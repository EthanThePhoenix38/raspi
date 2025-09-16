"""Main module for raspi remote configuration."""

from typing import Dict, Any


def get_system_info() -> Dict[str, Any]:
    """Get basic system information.

    Returns:
        Dictionary containing system information.
    """
    import platform
    import socket

    return {
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "architecture": platform.machine(),
    }


def main() -> None:
    """Main entry point for the raspi configuration tool."""
    info = get_system_info()
    print("System Information:")
    for key, value in info.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
