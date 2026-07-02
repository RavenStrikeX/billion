# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: HealthTrack
def calculate_monthly_stats(records):
    from datetime import datetime, timedelta
    
    if not records:
        return {}
    
    stats = {}
    current_month_start = None
    month_records = []
    
    for record in sorted(records, key=lambda x: x['timestamp'], reverse=True):
        date = record.get('date') or record.get('timestamp', datetime.now()).date()
        
        if not current_month_start or (date - current_month_start).days > 30:
            if month_records:
                stats[current_month_start.strftime('%Y-%m')] = {
                    'count': len(month_records),
                    'avg_value': sum(r.get('value', 1) for r in month_records) / max(len(month_records), 1),
                    'min_date': min(r['date'] for r in month_records).strftime('%d.%m'),
                    'max_date': max(r['date'] for r in month_records).strftime('%d.%m')
                }
            current_month_start = date
            month_records = []
        
        if (current_month_start and (date - current_month_start).days <= 30):
            month_records.append(record)
    
    # Process the last batch of records for the current month
    if month_records:
        stats[current_month_start.strftime('%Y-%m')] = {
            'count': len(month_records),
            'avg_value': sum(r.get('value', 1) for r in month_records) / max(len(month_records), 1),
            'min_date': min(r['date'] for r in month_records).strftime('%d.%m'),
            'max_date': max(r['date'] for r in month_records).strftime('%d.%m')
        }
    
    return stats
