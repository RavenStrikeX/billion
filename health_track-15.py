# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: HealthTrack
def calculate_weekly_stats(records):
    from datetime import date, timedelta
    if not records: return {}
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(weeks=1) - timedelta(days=1)
    filtered = [r for r in records if week_start <= r['date'] <= week_end]
    stats = {'count': len(filtered), 'avg_blood_pressure': None, 'avg_sleep_hours': None}
    bp_values = []
    sleep_values = []
    notes = {}
    habits_done = set()
    for rec in filtered:
        if 'blood_pressure' in rec and rec['blood_pressure']:
            try:
                systolic, diastolic = map(int, str(rec['blood_pressure']).split('/'))
                bp_values.append((systolic + diastolic) / 2)
            except ValueError: pass
        if 'sleep_hours' in rec and rec['sleep_hours'] is not None:
            sleep_values.append(float(rec['sleep_hours']))
        if 'note' in rec: notes[rec['date']] = rec['note']
        for habit, done in rec.get('habits', {}).items():
            if done: habits_done.add(habit)
    stats['avg_blood_pressure'] = sum(bp_values)/len(bp_values) if bp_values else None
    stats['avg_sleep_hours'] = sum(sleep_values)/len(sleep_values) if sleep_values else None
    stats['habits_completion_rate'] = len(habits_done)/max(len(records),1)*100 if records else 0.0
    return stats
