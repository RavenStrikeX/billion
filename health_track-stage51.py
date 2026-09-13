# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: HealthTrack
def log_data_change(change_type, data_key, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
    log_entry = {
        'timestamp': timestamp,
        'change_type': change_type,
        'data_key': data_key
    }
    data.setdefault('change_log', []).append(log_entry)
    return log_entry

def add_measurements(measurement_data, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
    log_data_change('measurements_added', 'measurements', timestamp)
    measurements.setdefault('data', []).append(measurement_data)
    return measurements['data'][-1]

def add_habit(habit_name, habit_data, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
    log_data_change('habit_added', habit_name, timestamp)
    habits.setdefault('data', []).append(habit_data)
    return habits['data'][-1]

def add_note(note_text, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
    log_data_change('note_added', 'notes', timestamp)
    notes.setdefault('data', []).append({'text': note_text, 'timestamp': timestamp})
    return notes['data'][-1]
