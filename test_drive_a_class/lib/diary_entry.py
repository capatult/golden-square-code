from math import ceil

class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   `title`, string
        #   `contents`, string
        if not isinstance(title, str):
            raise TypeError("`title` argument was not a string.")
        if not isinstance(contents, str):
            raise TypeError("`contents` argument was not a string.")
        self._title = title
        self._contents = contents

    def format(self):
        # Returns:
        #   a formatted diary entry
        #   e.g. "My Title: These are the contents"
        if self._title and self._contents:
            formatted = f"{self._title}:\n{self._contents}"
        elif (not self._title) and self._contents:
            formatted = f"(Untitled entry)\n{self._contents}"
        elif self._title and (not self._contents):
            formatted = f"{self._title} (Entry contents empty)"
        else:
            formatted = "(Untitled entry, contents empty)"
        return formatted

    def count_words(self):
        # Returns:
        #   integer: the number of words in the diary entry
        #
        # I interpret the above to mean the number of words in the entry's *contents*.
        return len(self._contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   `wpm`, integer: how many words the user can read per minute
        # Returns:
        #   integer: a resulting estimate of the reading time for the contents
        if (not isinstance(wpm, int)) or wpm <= 0:
            raise Exception("`wpm` argument was not a positive integer.")
        return ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   `wpm`, integer: how many words the user can read per minute
        #   `minutes`, integer: how many minutes the user wishes to read for
        # Returns:
        #   string: an appropriate chunk of self's contents for the user to read
        # 
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        if (not isinstance(wpm, int)) or wpm <= 0:
            raise Exception("`wpm` argument was not a positive integer.")
        if (not isinstance(minutes, int)) or minutes < 0:
            raise Exception("`minutes` argument was not a non-negative integer.")
        if minutes == 0:
            return ""
        else:
            return self._contents