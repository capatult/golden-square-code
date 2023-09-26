

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

    def reading_time(self, wpm):
        if (not isinstance(wpm, int)) or wpm <= 0:
            raise Exception("`wpm` argument was not a positive integer.")
        return sum(
            entry.reading_time(wpm)
            for entry in self._entries
        )

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if (not isinstance(wpm, int)) or wpm <= 0:
            raise Exception("`wpm` argument was not a positive integer.")
        if (not isinstance(minutes, int)) or minutes < 0:
            raise Exception("`minutes` argument was not a non-negative integer.")
        entry_with_reading_time_tuples = (
            (entry, entry.reading_time(wpm))
            for entry in self._entries
        )
        entry_tuples_satisfying_time_limit = (
            entry_tuple for entry_tuple in entry_with_reading_time_tuples
            if entry_tuple[1] <= minutes
        )
        best_entry, __ = max(
            entry_tuples_satisfying_time_limit,
            default = (None, None),
            key = lambda entry_tuple: entry_tuple[1]
        )
        return best_entry
