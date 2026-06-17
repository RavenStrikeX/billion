# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: HealthTrack
from typing import Literal, Optional
from datetime import date

def filter_health_records(
    records: list[dict],
    status: Optional[Literal["good", "bad", "neutral"]] = None,
    category: Optional[str] = None,
    tag: Optional[str] = None,
) -> list[dict]:
    filtered = []
    for record in records:
        if status is not None and record.get("status") != status:
            continue
        if category is not None and record.get("category") != category:
            continue
        if tag is not None and tag not in record.get("tags", []):
            continue
        filtered.append(record)
    return filtered

def generate_weekly_report(
    records: list[dict],
    start_date: date,
    end_date: date,
) -> dict[str, any]:
    week_records = [r for r in records if start_date <= r.get("date", date.today()) < (end_date + timedelta(days=1))]
    status_counts = {"good": 0, "bad": 0, "neutral": 0}
    category_counts: dict[str, int] = {}
    tags_set: set[str] = set()
    
    for record in week_records:
        status = record.get("status", "neutral")
        if status in status_counts:
            status_counts[status] += 1
        
        cat = record.get("category")
        if cat:
            category_counts[cat] = category_counts.get(cat, 0) + 1
        
        for t in record.get("tags", []):
            tags_set.add(t)
    
    return {
        "total_records": len(week_records),
        "status_distribution": status_counts,
        "category_distribution": category_counts,
        "unique_tags": list(tags_set),
        "average_score": sum(r.get("score", 0) for r in week_records if isinstance(r.get("score"), (int, float))) / max(len(week_records), 1)
    }
