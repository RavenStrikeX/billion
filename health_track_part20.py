# === Stage 20: Добавь восстановление записей из архива ===
# Project: HealthTrack
import json, os

ARCHIVE_FILE = "health_archive.json"

def restore_from_archive():
    if not os.path.exists(ARCHIVE_FILE):
        return {"status": "no archive", "message": "Архив не найден."}
    try:
        with open(ARCHIVE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            return {"status": "corrupt", "message": "Неверный формат архива."}
        restored = []
        for entry in data:
            record_type = entry.get("type")
            content = entry.get("content", {})
            metadata = entry.get("metadata", {})

            if record_type == "vital_record":
                restored.append({
                    "id": str(metadata.get("date", "")),
                    **content,
                    "_source": "archive"
                })
            elif record_type == "habit_log":
                restored.append({
                    "date": metadata.get("date"),
                    "habits": content,
                    "_source": "archive"
                })
            elif record_type == "note":
                restored.append({
                    "title": metadata.get("title", ""),
                    "text": content.get("text", ""),
                    "_source": "archive"
                })
            elif record_type == "weekly_report":
                restored.append({
                    "date": metadata.get("date"),
                    **content,
                    "_source": "archive"
                })
        return {"status": "ok", "restored_count": len(restored), "records": restored}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    result = restore_from_archive()
    print(json.dumps(result, indent=2, ensure_ascii=False))
