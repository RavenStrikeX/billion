# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: HealthTrack
def export_state():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "metrics": metrics,
        "habits": habits,
        "notes": notes,
        "weekly_reports": weekly_reports
    }
    return json.dumps(state, indent=2)
