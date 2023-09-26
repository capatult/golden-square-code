import pytest
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

"""
When the `reading_time` method of a Diary instance with an entry is called
And the `wpm` argument provided is invalid
It raises an appropriate exception
"""
def test_estimating_total_reading_time_with_invalid_wpm_raises_error():
    diary = Diary()
    entry = DiaryEntry("An entry", "being added should not prevent the exception from being raised.")
    diary.add(entry)
    with pytest.raises(Exception) as e_wpm_zero:
        diary.reading_time(0)
    with pytest.raises(Exception) as e_wpm_negative:
        diary.reading_time(-1)
    with pytest.raises(Exception) as e_wpm_non_integer:
        diary.reading_time(None)
    for e in (e_wpm_zero, e_wpm_negative, e_wpm_non_integer):
        assert str(e.value) == "`wpm` argument was not a positive integer."


"""
When two diary entries are added to a new Diary instance
And the `reading_time` method of the Diary instance is called with valid wpm
It returns the sum of the reading times of the individual diary entries
(It does not calculate the result based on the word count of the entire diary)
"""
def test_can_estimate_reading_time_of_diary():
    diary = Diary()
    entry_1 = DiaryEntry("First entry", "This is the first entry")
    entry_2 = DiaryEntry("Second entry", "This is the second entry, which will be added after the first entry")
    diary.add(entry_1)  # contents is 5 words long
    diary.add(entry_2)  # contents is 13 words long
    estimated_totals = []
    for wpm in (1, 5, 100):
        estimated_totals.append(diary.reading_time(wpm))
    assert estimated_totals == [
        18,  # == ceil(5 / 1) + ceil(13 / 1) = 5 + 13
        4,   # == ceil(5 / 5) + ceil(13 / 5) = 1 + 3
        2,   # == ceil(5 / 100) + ceil(13 / 100) = 1 + 1
    ]

"""
When the `find_best_entry_for_reading_time` method of a Diary instance with an entry is called
And the `wpm` argument provided is invalid
It raises an appropriate exception
"""
def test_finding_best_entry_for_reading_time_with_invalid_wpm_raises_error():
    diary = Diary()
    entry = DiaryEntry("An entry", "being added should not prevent the exception from being raised.")
    diary.add(entry)
    with pytest.raises(Exception) as e_wpm_zero:
        diary.find_best_entry_for_reading_time(0, 1)
    with pytest.raises(Exception) as e_wpm_negative:
        diary.find_best_entry_for_reading_time(-1, 1)
    with pytest.raises(Exception) as e_wpm_non_integer:
        diary.find_best_entry_for_reading_time(None, 1)
    for e in (e_wpm_zero, e_wpm_negative, e_wpm_non_integer):
        assert str(e.value) == "`wpm` argument was not a positive integer."

"""
When the `find_best_entry_for_reading_time` method of a Diary instance with an entry is called
And the `minutes` argument provided is invalid
It raises an appropriate exception
"""
def test_finding_best_entry_for_reading_time_with_invalid_minutes_raises_error():
    diary = Diary()
    entry = DiaryEntry("An entry", "being added should not prevent the exception from being raised.")
    diary.add(entry)
    with pytest.raises(Exception) as e_minutes_negative:
        diary.find_best_entry_for_reading_time(10, -1)
    with pytest.raises(Exception) as e_minutes_non_integer:
        diary.find_best_entry_for_reading_time(10, None)
    for e in (e_minutes_negative, e_minutes_non_integer):
        assert str(e.value) == "`minutes` argument was not a non-negative integer."

"""
When we create a Diary instance and add some entries to it
And the `find_best_entry_for_reading_time` method of the Diary instance is called with valid wpm
And there does not exist any diary entry with estimated reading time at most the value of argument `minutes`
It returns None
(It does not raise an exception)
"""
def test_find_best_entry_for_reading_time_returns_none_if_no_valid_entry_exists():
    diary = Diary()
    entries = [
        DiaryEntry("Three word entry", "Just three words!"),
        DiaryEntry("Eight word entry", "At eight words, this is the longest entry."),
        DiaryEntry("Older five word entry", "This is five words long."),
        DiaryEntry("Two word entry", "Two words."),
        DiaryEntry("Newer five word entry", "Another five words in here."),
    ]
    for entry in entries:
        diary.add(entry)
    best_entry_at_most_0_minutes = diary.find_best_entry_for_reading_time(1, 0)
    best_entry_at_most_1_minute = diary.find_best_entry_for_reading_time(1, 1)
    assert best_entry_at_most_0_minutes is None
    assert best_entry_at_most_1_minute is None

"""
When we create a Diary instance and add some entries to it
And the `find_best_entry_for_reading_time` method of the Diary instance is called with valid wpm
And there exists at least one diary entry with estimated reading time <= value of `minutes` argument
It returns the oldest diary entry whose estimated reading time is equal to the maximum of
    the estimated reading times amongst all such diary entries satisfying this criterion
"""
def test_can_get_valid_best_entry_for_reading_time_if_any_such_entry_exists():
    diary = Diary()
    entries = [
        DiaryEntry("Three word entry", "Just three words!"),
        DiaryEntry("Eight word entry", "At eight words, this is the longest entry."),
        DiaryEntry("Older five word entry", "This is five words long."),
        DiaryEntry("Two word entry", "Two words."),
        DiaryEntry("Newer five word entry", "Another five words in here."),
    ]
    for entry in entries:
        diary.add(entry)
    best_entry_at_most_2_minutes = diary.find_best_entry_for_reading_time(1, 2)
    best_entry_at_most_3_minutes = diary.find_best_entry_for_reading_time(1, 3)
    best_entry_at_most_4_minutes = diary.find_best_entry_for_reading_time(1, 4)
    best_entry_at_most_5_minutes = diary.find_best_entry_for_reading_time(1, 5)
    assert best_entry_at_most_2_minutes == entries[3]
    assert best_entry_at_most_3_minutes == entries[0]
    assert best_entry_at_most_4_minutes == entries[0]
    assert best_entry_at_most_5_minutes == entries[2]

"""
When we create a Diary instance
And add one diary entry with a word count of 0 to it
And call the `find_best_entry_for_reading_time` method with a `minutes` value of 0
It returns that diary entry
(It does not return None)
"""
def test_entry_with_zero_word_contents_is_valid_best_entry_for_zero_minutes_reading_time():
    diary = Diary()
    entry = DiaryEntry("Entry with empty contents", "")
    diary.add(entry)
    best_entry_at_most_0_minutes = diary.find_best_entry_for_reading_time(1, 0)
    assert best_entry_at_most_0_minutes == entry
