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
    assert False

"""
If the contents of the diary entry are empty
When we count the words in the entry
It returns 0
"""
def test_word_count_is_zero_if_diary_entry_contents_empty():
    assert False

"""
When we count the words in the entry
It returns the correct number of words
"""
def test_word_count_of_diary_entry_contents_correct():
    assert False

"""
If some words in the diary entry are connected by non-whitespace characters
    e.g. "hello-world:good.morning"
When we count the words in the entry
The groups of such words are treated as a single word each
It returns the correct number of words according to this behaviour
"""
def test_words_only_delineated_by_whitespace_for_word_count_purposes():
    assert False

"""
If the contents of the diary entry are empty
When we estimate the reading time for the contents
It returns 0 for any positive value of wpm
"""
def test_estimated_reading_time_is_zero_minutes_for_empty_contents():
    assert False

"""
When we estimate the reading time for the contents
And we provide 0 or a negative number as the value of `wpm`
Or we provide a non-integer object as the value of `wpm`
It raises an exception
"""
def test_esimating_reading_time_with_invalid_wpm_raises_error():
    assert False

"""
When we estimate the reading time for the contents
The esimated reading time in minutes is rounded up to the nearest whole number
It returns this rounded estimate
"""
def test_estimated_reading_time_rounded_up_to_nearest_minute():
    assert False

"""
If the contents of the diary entry are empty
When we request a reading chunk
It always returns an empty string
"""
def test_reading_chunk_always_empty_if_diary_entry_contents_empty():
    assert False

"""
When we request a reading chunk
And we provide 0 as the value of `minutes`
It returns an empty string
"""
def test_reading_chunk_empty_if_minutes_argument_is_zero():
    assert False

"""
When we request a reading chunk
And we provide 0 or a negative number as the value of `wpm`
Or we provide a non-integer object as the value of `wpm`
It raises an exception
"""
def test_requesting_reading_chunk_with_invalid_wpm_raises_error():
    assert False

"""
When we request a reading chunk
And we provide a negative number as the value of `minutes`
Or we provide a non-integer object as the value of `wpm`
It raises an exception
"""
def test_requesting_reading_chunk_with_invalid_minutes_raises_error():
    assert False

"""
When we repeatedly request a reading chunk
And provide values for `wpm` and `minutes` which cause the entire contents to be returned
It returns the entire contents each time we request
"""
def test_requesting_reading_chunk_encompassing_all_contents_always_returns_all_contents():
    assert False

"""
When we repeatedly request a reading chunk
It returns the next unread chunk of the appropriate size each time
It also restarts from the beginning once requested chunks have covered all of contents
"""
def test_repeated_reading_chunk_requests_return_successive_chunks_with_correct_restarts():
    assert False

"""
When we repeatedly request a reading chunk
And request a chunk which returns to the end of contents but overlap
It still restarts correctly on the next chunk request instead of returning an empty string
"""
def test_repeated_reading_chunk_requests_restart_correctly_and_do_not_return_empty_chunk():
    assert False
