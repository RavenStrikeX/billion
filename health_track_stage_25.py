# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: HealthTrack
def parse_date_safe(raw, fmt='%Y-%m-%d'):
    """Parse a date string and return (datetime.date, error_message)."""
    raw = raw.strip()
    if not raw:
        return None, 'Дата не может быть пустой.'

    for candidate in [fmt, '%d.%m.%Y', '%d/%m/%Y']:
        try:
            dt = datetime.strptime(raw, candidate)
            return dt.date(), None
        except ValueError:
            continue

    # Fallback to ISO format with lenient handling
    try:
        dt = datetime.fromisoformat(raw.replace(' ', 'T'))
        return dt.date(), None
    except Exception as e:
        return None, f'Не удалось распознать дату "{raw}". Форматы: dd.MM.yyyy, dd.mm.yyyy, yyyy-mm-dd.'
