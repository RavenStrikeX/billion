# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: HealthTrack
def print_project_metrics():
    """Print key project metrics."""
    import os
    lines = open(__file__).read().splitlines()
    total_lines = len(lines)
    docstring_count = sum(1 for l in lines if (l.strip().startswith('"""') and not l.strip().startswith('#')))
    class_count = sum(1 for l in lines if re.search(r'^class\s+\w+)', l))
    func_count = sum(1 for l in lines if re.search(r'^def\s+\w+', l))
    print(f"Total lines: {total_lines}")
    print(f"Classes: {class_count}")
    print(f"Functions: {func_count}")
    print(f"Documentation blocks: {docstring_count}")

if __name__ == "__main__":
    import re  # noqa: E402
    print_project_metrics()
