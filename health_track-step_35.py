# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: HealthTrack
def next_action(state: dict) -> str:
    """Return a short recommendation based on the current health state."""
    actions = []
    if state.get("sleep_hours", 0) < 7:
        actions.append("💤 Sleep more — aim for at least 7 hours.")
    if state.get("water_liters", 0) < 2.0:
        actions.append("💧 Drink more water today (≥2 L).")
    if state.get("exercise_minutes", 0) == 0 and not state.get("resting_today"):
        actions.append("🏃 Do a short walk or stretch session.")
    if state.get("mood", "") in ("low", "tired", "stressed") and state.get("meditation_minutes", 0) < 10:
        actions.append("🧘 Try 5–10 minutes of breathing/meditation.")
    if not state.get("note_today"):
        actions.append("✍️ Write a brief note about how you feel today.")
    return "; ".join(actions) if actions else "✅ Keep up the good work!"
