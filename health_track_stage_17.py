# === Stage 17: Добавь группировку записей по категориям ===
# Project: HealthTrack
from collections import defaultdict, Counter

def group_entries_by_category(entries):
    grouped = defaultdict(list)
    for entry in entries:
        cat = entry.get('category', 'general')
        grouped[cat].append(entry)
    
    sorted_categories = sorted(grouped.keys(), key=lambda c: len(grouped[c]), reverse=True)
    return {cat: group_entries[grouped[cat]] for cat, group_entries in grouped.items()}
