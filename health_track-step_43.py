# === Stage 43: Добавь пагинацию длинных списков ===
# Project: HealthTrack
class PaginatedView:
    """Компактная пагинация для длинных списков."""
    def __init__(self, data, page_size=10):
        self.data = data
        self.page_size = page_size
        self.current_page = 0

    def _total_pages(self):
        return max(1, len(self.data) // self.page_size + (1 if len(self.data) % self.page_size else 0))

    def page(self, page=1):
        page = max(1, min(page, self._total_pages()))
        start = (page - 1) * self.page_size
        return self.data[start:start + self.page_size], page, self._total_pages()
