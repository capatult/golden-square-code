

class DiaryEntry:
    def __init__(self, title, contents):
        self._title = title
        self._contents = contents

    def count_words(self):
        return len(self._contents.split())