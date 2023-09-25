

class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return list(self._entries)

    def count_words(self):
        return sum(
            entry.count_words()
            for entry in self._entries
        )
