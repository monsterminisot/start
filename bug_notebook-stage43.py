# === Stage 43: Добавь пагинацию длинных списков ===
# Project: BugNotebook
class PaginatedView:
    def __init__(self, data, page_size=10):
        self.data = data
        self.page_size = page_size
        self._pages = [data[i:i + page_size] for i in range(0, len(data), page_size)]

    @property
    def total_pages(self):
        return (len(self.data) + self.page_size - 1) // self.page_size

    def get_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page {page_num} out of range (1..{self.total_pages})")
        return self._pages[page_num - 1]

    def __iter__(self):
        for page in self._pages:
            yield from page

    def __len__(self):
        return len(self.data)
