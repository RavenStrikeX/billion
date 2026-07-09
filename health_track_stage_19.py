# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: HealthTrack
def archive_entries():
    """Move completed or old entries to an archive list."""
    active = []
    archived = []
    for entry in entries:
        if entry['completed']:
            archived.append(entry.copy())
        elif 'date' in entry and (entry['date'] < today - timedelta(days=30)):
            archived.append(entry.copy())
        else:
            active.append(entry)
    return archived
