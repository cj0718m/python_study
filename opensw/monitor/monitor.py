"""A simple real-time CPU and memory monitor for Windows."""

import os
import time

try:
    import psutil
except ImportError:
    raise SystemExit("psutil is required. Install it with: python -m pip install psutil")


def format_bytes(value: int) -> str:
    """Convert a byte value to a readable unit."""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if value < 1024 or unit == "TB":
            return f"{value:.2f} {unit}"
        value /= 1024
    return f"{value:.2f} TB"


def show_monitor() -> None:
    """Continuously show the current CPU and memory state."""
    psutil.cpu_percent(interval=None)

    try:
        while True:
            cpu = psutil.cpu_percent(interval=None)
            memory = psutil.virtual_memory()

            os.system("cls")
            print("=" * 48)
            print("          REAL-TIME SYSTEM MONITOR")
            print("=" * 48)
            print(f"CPU usage:          {cpu:6.1f}%")
            print(f"Memory usage:       {memory.percent:6.1f}%")
            print(f"Used memory:        {format_bytes(memory.used):>10}")
            print(f"Available memory:   {format_bytes(memory.available):>10}")
            print("-" * 48)
            print("Refreshing every second. Press Ctrl+C to stop.")

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitor stopped.")


if __name__ == "__main__":
    show_monitor()
