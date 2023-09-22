import pytest
from lib.diary_entry import *
DiaryEntry = DiaryEntry  # This makes pylance behave a bit better

# Template:
# [If <a condition which might apply>]
# When <thing happens>
# [And <another thing happens>]
# [The <changes to state>]
# [It returns <return value(s) given>]

"""
When a diary entry is created
The title and contents attributes should exist
"""
def test_diary_entry_has_title_and_contents_attributes():
    diary_entry = DiaryEntry("", "")
    assert (diary_entry._title == "") and (diary_entry._contents == "")

"""
When a diary entry is created
The title and contents attributes should reflect the parameters
"""
def test_diary_entry_attributes_have_correct_values_after_init():
    my_title = "Hello"
    my_contents = "Dear Diary, Hello World!"
    diary_entry = DiaryEntry(my_title, my_contents)
    assert (
        diary_entry._title == "Hello"
    ) and (
        diary_entry._contents == "Dear Diary, Hello World!"
    )

"""
When a diary entry is created with a non-string argument
It raises an exception
"""
def test_diary_entry_init_arguments_must_be_strings():
    with pytest.raises(Exception) as e_title:
        diary_entry_with_invalid_title = DiaryEntry(None, "")
    with pytest.raises(Exception) as e_contents:
        diary_entry_with_invalid_contents = DiaryEntry("", None)
    assert str(e_title.value) == "`title` argument was not a string."
    assert str(e_contents.value) == "`contents` argument was not a string."

"""
When we format the diary entry
It returns the correct formatted diary entry
"""
def test_format_returns_correctly_formatted_diary_entry():
    diary_entry = DiaryEntry("My Day", "Today was a good day")
    result = diary_entry.format()
    assert result == "My Day:\nToday was a good day"

"""
If the title or contents of the diary entry are empty
When we format the diary entry
The appropriate placeholder notice is used in place of the title or contents
It returns this
"""
def test_format_returns_formatted_entry_with_correct_placeholders():
    diary_entries = [
        DiaryEntry("", "Some contents"),
        DiaryEntry("Some title", ""),
        DiaryEntry("", ""),
    ]
    actual_formatted_entries = [
        diary_entry.format()
        for diary_entry in diary_entries
    ]
    expected_formatted_entries = [
        "(Untitled entry)\nSome contents",
        "Some title (Entry contents empty)",
        "(Untitled entry, contents empty)",
    ]
    assert all(
        actual == expected
        for actual, expected in zip(
            actual_formatted_entries,
            expected_formatted_entries
        )
    )

"""
If the contents of the diary entry are empty
When we count the words in the entry
It returns 0
"""
def test_word_count_is_zero_if_diary_entry_contents_empty():
    diary_entry = DiaryEntry("", "")
    word_count = diary_entry.count_words()
    assert word_count == 0

"""
When we count the words in the entry
It returns the correct number of words
"""
def test_word_count_of_diary_entry_contents_correct():
    contents = "The quick brown fox jumped over the lazy dog."
    diary_entry = DiaryEntry("", contents)
    word_count = diary_entry.count_words()
    assert word_count == 9

"""
If some words in the diary entry are connected by non-whitespace characters
    e.g. "hello-world:good.morning"
When we count the words in the entry
The groups of such words are treated as a single word each
It returns the correct number of words according to this behaviour
"""
def test_words_only_delineated_by_whitespace_for_word_count_purposes():
    contents = """
Hello World!
This-will>all.be?interpreted.as.one_word

Blank lines don't increase word count but do count as
whitespace
"""
    diary_entry = DiaryEntry("", contents)
    word_count = diary_entry.count_words()
    assert word_count == 14

"""
If the contents of the diary entry are empty
When we estimate the reading time for the contents
It returns 0 for any positive value of wpm
"""
def test_estimated_reading_time_is_zero_minutes_for_empty_contents():
    diary_entry = DiaryEntry("My title", "")
    estimated = diary_entry.reading_time(1)
    assert estimated == 0

"""
When we estimate the reading time for the contents
And we provide 0 or a negative number as the value of `wpm`
Or we provide a non-integer object as the value of `wpm`
It raises an exception
"""
def test_esimating_reading_time_with_invalid_wpm_raises_error():
    diary_entry = DiaryEntry("Title", "Some contents")
    with pytest.raises(Exception) as e_wpm_zero:
        diary_entry.reading_time(0)
    with pytest.raises(Exception) as e_wpm_negative:
        diary_entry.reading_time(-1)
    with pytest.raises(Exception) as e_wpm_non_integer:
        diary_entry.reading_time(None)
    assert all(
        str(e.value) == "`wpm` argument was not a positive integer."
        for e in (e_wpm_zero, e_wpm_negative, e_wpm_non_integer)
    )

"""
When we estimate the reading time for the contents
The esimated reading time in minutes is rounded up to the nearest whole number
It returns this rounded estimate
"""
def test_estimated_reading_time_rounded_up_to_nearest_minute():
    diary_entry_1 = DiaryEntry("My title", "hello")
    estimated_1 = diary_entry_1.reading_time(10000)
    diary_entry_2 = DiaryEntry("My title", "a b c d e; f g h i j;")
    estimated_2 = diary_entry_2.reading_time(5)
    assert (estimated_1 == 1) and (estimated_2 == 2)

"""
If the contents of the diary entry are empty
When we request a reading chunk
It always returns an empty string
"""
def test_reading_chunk_always_empty_if_diary_entry_contents_empty():
    diary_entry = DiaryEntry("My title", "")
    chunks = [
        diary_entry.reading_chunk(1, 0),
        diary_entry.reading_chunk(1, 1),
        diary_entry.reading_chunk(1, 10),
    ]
    assert all(chunk == "" for chunk in chunks)
    
"""
When we request a reading chunk
And we provide 0 as the value of `minutes`
It returns an empty string
"""
def test_reading_chunk_empty_if_minutes_argument_is_zero():
    diary_entries = [
        DiaryEntry("", contents) for contents in (
            "",
            "hello",
            "dear diary, today was a good day",
        )
    ]
    chunks = [
        diary_entry.reading_chunk(10, 0)
        for diary_entry in diary_entries
    ]
    assert all(chunk == "" for chunk in chunks)

"""
When we request a reading chunk
And we provide 0 or a negative number as the value of `wpm`
Or we provide a non-integer object as the value of `wpm`
It raises an exception
"""
def test_requesting_reading_chunk_with_invalid_wpm_raises_error():
    diary_entry = DiaryEntry("Title", "Some contents")
    with pytest.raises(Exception) as e_wpm_zero:
        diary_entry.reading_chunk(0, 1)
    with pytest.raises(Exception) as e_wpm_negative:
        diary_entry.reading_chunk(-1, 1)
    with pytest.raises(Exception) as e_wpm_non_integer:
        diary_entry.reading_chunk(None, 1)
    assert all(
        str(e.value) == "`wpm` argument was not a positive integer."
        for e in (e_wpm_zero, e_wpm_negative, e_wpm_non_integer)
    )

"""
When we request a reading chunk
And we provide a negative number as the value of `minutes`
Or we provide a non-integer object as the value of `wpm`
It raises an exception
"""
def test_requesting_reading_chunk_with_invalid_minutes_raises_error():
    diary_entry = DiaryEntry("Title", "Some contents")
    with pytest.raises(Exception) as e_minutes_negative:
        diary_entry.reading_chunk(10, -1)
    with pytest.raises(Exception) as e_minutes_non_integer:
        diary_entry.reading_chunk(10, None)
    assert all(
        str(e.value) == "`minutes` argument was not a non-negative integer."
        for e in (e_minutes_negative, e_minutes_non_integer)
    )

"""
When we repeatedly request a reading chunk
And provide values for `wpm` and `minutes` which cause the entire contents to be returned
It returns the entire contents each time we request
"""
def test_requesting_reading_chunk_encompassing_all_contents_always_returns_all_contents():
    contents = "This entry contains a total of eight words."
    diary_entry = DiaryEntry("Today's Entry", contents)
    chunks = []
    wpm_and_minutes = [
        (1, 100),  # up to 100 words
        (1, 10),   # up to 10 words
        (10, 1),   # up to 10 words
        (2, 4),    # up to 8 words
        (8, 1),    # up to 8 words
    ]
    for wpm, minutes in wpm_and_minutes:
        chunks.append(diary_entry.reading_chunk(wpm, minutes))
    assert all(
        chunk == contents
        for chunk in chunks
    )

# """
# When we repeatedly request a reading chunk
# It returns the next unread chunk of the appropriate size each time
# It also restarts from the beginning once requested chunks have covered all of contents
# """
# def test_repeated_reading_chunk_requests_return_successive_chunks_with_correct_restarts():
#     contents = "This is a longer diary entry containing a total of twelve words."
#     diary_entry = DiaryEntry

# """
# When we repeatedly request a reading chunk
# And request a chunk which returns to the end of contents but overlap
# It still restarts correctly on the next chunk request instead of returning an empty string
# """
# def test_repeated_reading_chunk_requests_restart_correctly_and_do_not_return_empty_chunk():
#     assert False
