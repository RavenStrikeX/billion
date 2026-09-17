# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: HealthTrack
def showFavorites():
    fav = db.get("favorites", [])
    if not fav:
        print("Избранных записей пока нет.")
        return
    print("\n=== Избранные записи ===")
    for i, ref in enumerate(fav, 1):
        print(f"[{i}] {ref}")
    print()

def toggleFavorite(idx):
    if idx < 1 or idx > len(db.get("favorites", [])):
        print("Неверный индекс избранного.")
        return
    ref = db.get("favorites", [])[idx - 1]
    if ref not in records:
        print("Запись не найдена.")
        return
    records[ref]["is_favorite"] = not records[ref].get("is_favorite", False)
    db["favorites"] = [r for r in db.get("favorites", []) if r != ref]
    if records[ref]["is_favorite"]:
        db["favorites"].append(ref)
    print(f"Избранный статус: {'✓ добавлен' if records[ref]['is_favorite'] else '✗ удалён'}.")
