# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: HealthTrack
def sort_records(records, key='date', reverse=False):
    if not records: return []
    def parse_date(r):
        try: return datetime.strptime(str(r[key]), '%Y-%m-%d %H:%M').timestamp()
        except: return 0
    if key == 'priority':
        priority_map = {'high': -1, 'medium': 0, 'low': 1}
        return sorted(records, key=lambda x: (x.get(key) in priority_map and priority_map[x[key]] or 2))
    elif key == 'name':
        return sorted(records, key=lambda x: str(x.get(key, '')).lower())
    else: # date
        return sorted(records, key=parse_date, reverse=reverse)
