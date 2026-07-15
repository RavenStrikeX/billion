# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: HealthTrack
def print_table(headers, rows):
    """Compact console table: aligns columns and prints a formatted grid."""
    col_count = len(headers)
    widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row if isinstance(row, list) else []):
            widths[i] = max(widths[i], len(str(val)))

    fmt = "  ".join(f"{{{i}:<{widths[i]}}}" for i in range(col_count))
    print(fmt.format(*headers))
    print("-".join("-" * w for w in widths))
    for row in rows:
        if isinstance(row, list):
            print(fmt.format(*row))
