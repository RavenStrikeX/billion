# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: HealthTrack
def tag_manager(self):
    """Добавление и удаление тегов для записей."""
    def add_tags(record, tags):
        if not isinstance(tags, list):
            tags = [tags]
        record.tags = set(record.tags) | {t.strip().lower() for t in tags}

    def remove_tags(record, tags):
        if not isinstance(tags, list):
            tags = [tags]
        record.tags -= {t.strip().lower() for t in tags}
