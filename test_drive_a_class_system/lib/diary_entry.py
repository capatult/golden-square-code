from math import ceil

class DiaryEntry:
    def __init__(self, title, contents):
        if not isinstance(title, str):
            raise TypeError("`title` argument was not a string.")
        if not isinstance(contents, str):
            raise TypeError("`contents` argument was not a string.")
        self._title = title
        self._contents = contents
        self._words_of_contents = self._contents.split()
        self._reading_progress = 0

    def count_words(self):
        return len(self._contents.split())

    def reading_time(self, wpm):
        if (not isinstance(wpm, int)) or wpm <= 0:
            raise Exception("`wpm` argument was not a positive integer.")
        return ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        if (not isinstance(wpm, int)) or wpm <= 0:
            raise Exception("`wpm` argument was not a positive integer.")
        if (not isinstance(minutes, int)) or minutes < 0:
            raise Exception("`minutes` argument was not a non-negative integer.")
        if minutes == 0:
            return ""
        desired_words_in_chunk = wpm * minutes
        words_in_chunk = self._words_of_contents[
            self._reading_progress
            : self._reading_progress + desired_words_in_chunk
        ]
        self._reading_progress += desired_words_in_chunk
        if self._reading_progress >= len(self._words_of_contents):
            self._reading_progress = 0
        return " ".join(words_in_chunk)
