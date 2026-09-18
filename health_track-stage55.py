# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: HealthTrack
def soft_dedup_check(records, new_record):
    """Soft duplicate check: returns (is_duplicate, conflict_type) where conflict_type is
    'date', 'metric', 'habit', or 'note'. For mixed-type records, compare only the type
    that matches new_record's kind."""
    new_kind = new_record.get('kind')
    for rec in records:
        if rec.get('kind') != new_kind:
            continue
        if new_record.get('date') == rec.get('date'):
            return True, 'date'
        if new_record.get('metric') == rec.get('metric'):
            return True, 'metric'
        if new_record.get('habit') == rec.get('habit'):
            return True, 'habit'
        if new_record.get('note') == rec.get('note'):
            return True, 'note'
    return False, None
