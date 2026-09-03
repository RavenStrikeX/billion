# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: HealthTrack
import shutil
from datetime import datetime

def backup_data_file(data_file_path, backup_dir="backups"):
    """Create a timestamped backup of the data file.

    Args:
        data_file_path: Path to the current data file.
        backup_dir: Directory where backups are stored (default: 'backups/').

    Returns:
        Path to the created backup file, or None if backup failed.
    """
    try:
        if not shutil.which(shutil):
            import os
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}_{os.path.basename(data_file_path)}")
        shutil.copy2(data_file_path, backup_path)
        return backup_path
    except Exception as e:
        print(f"Backup failed: {e}")
        return None
