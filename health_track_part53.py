# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: HealthTrack
import json
from pathlib import Path
from datetime import datetime


def import_records(file_path: str) -> list[dict]:
    """Import health records from a simple JSON text file."""
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and 'records' in data:
                return data['records']
            else:
                print("Invalid file format. Expected a list or dict with 'records' key.")
                return []
        except json.JSONDecodeError:
            print("Error: File contains invalid JSON.")
            return []
