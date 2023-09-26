

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
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        if (not isinstance(wpm, int)) or wpm <= 0:
            raise Exception("`wpm` argument was not a positive integer.")
        if (not isinstance(minutes, int)) or minutes < 0:
            raise Exception("`minutes` argument was not a non-negative integer.")
        best_entry = max(
            (
                entry for entry in self._entries
                if entry.reading_time(wpm) <= minutes
            ),
            default = None,
            key = lambda entry: entry.reading_time(wpm)
        )
        return best_entry
