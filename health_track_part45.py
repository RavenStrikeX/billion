# === Stage 45: Добавь восстановление из резервной копии ===
# Project: HealthTrack
import json, os

def load_backup(backup_path="health_backup.json"):
    if not os.path.exists(backup_path):
        return False
    with open(backup_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, dict):
        return False
    keys = {'indicators', 'habits', 'notes', 'reports', 'settings'}
    if not keys.issubset(data.keys()):
        return False
    return True

def restore_backup(backup_path="health_backup.json"):
    if not load_backup(backup_path):
        print("Ошибка: файл резервной копии не найден или некорректен.")
        return False
    with open(backup_path, 'r', encoding='utf-8') as f:
        backup = json.load(f)
    for key in backup:
        if key in globals():
            globals()[key].update(backup[key])
        else:
            globals()[key] = backup[key]
    print("Резервная копия успешно восстановлена.")
    return True

def save_backup():
    data = {
        'indicators': indicators,
        'habits': habits,
        'notes': notes,
        'reports': reports,
        'settings': settings
    }
    with open('health_backup.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Резервная копия сохранена в health_backup.json")
