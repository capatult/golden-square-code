from lib.diary import Diary
from lib.diary_entry import DiaryEntry


"""
When two diary entries are added to a new Diary instance
And the `all` method of the Diary instance is called
It returns a list of those instances of DiaryEntry
"""
def test_can_add_and_list_all_diary_entries_of_diary():
    diary = Diary()
    entry_1 = DiaryEntry("First entry", "This is the first entry")
    entry_2 = DiaryEntry("Second entry", "This is the second entry, which will be added after the first entry")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.all()
    assert result == [entry_1, entry_2]

"""
When two diary entries are added to a new Diary instance
And the `count_words` method of the Diary instance is called
It returns the sum of the word count across all stored diary entries
"""
def test_can_find_combined_word_count_of_all_diary_entries_of_diary():
    diary = Diary()
    entry_1 = DiaryEntry("First entry", "This is the first entry")
    entry_2 = DiaryEntry("Second entry", "This is the second entry, which will be added after the first entry")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.count_words()
    assert result == 18  # == 5 + 13