# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: HealthTrack
import sys

if sys.platform != "win32":
    colors = {
        "RESET": "\033[0m",
        "RED": "\033[91m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "BLUE": "\033[94m",
        "MAGENTA": "\033[95m",
        "CYAN": "\033[96m",
        "WHITE": "\033[97m",
        "BOLD": "\033[1m",
        "DIM": "\033[2m",
    }
else:
    colors = {
        "RESET": "",
        "RED": "",
        "GREEN": "",
        "YELLOW": "",
        "BLUE": "",
        "MAGENTA": "",
        "CYAN": "",
        "WHITE": "",
        "BOLD": "",
        "DIM": "",
    }

def c(text: str, key: str) -> str:
    return colors.get(key, "") + text + colors.get("RESET", "")
