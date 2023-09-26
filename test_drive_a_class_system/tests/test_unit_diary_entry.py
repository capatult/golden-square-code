import pytest
from lib.diary_entry import DiaryEntry
DiaryEntry = DiaryEntry  # This makes pylance behave a bit better

def convert_to_single_space_joined_words(string):
    return " ".join(string.split())

def test_diary_entry_has_title_and_contents_attributes():
    diary_entry = DiaryEntry("", "")
    assert diary_entry._title == ""
    assert diary_entry._contents == ""

def test_diary_entry_attributes_have_correct_values_after_init():
    my_title = "Hello"
    my_contents = "Dear Diary, Hello World!"
    diary_entry = DiaryEntry(my_title, my_contents)
    assert diary_entry._title == "Hello"
    assert diary_entry._contents == "Dear Diary, Hello World!"

def test_diary_entry_init_arguments_must_be_strings():
    with pytest.raises(Exception) as e_title:
        diary_entry_with_invalid_title = DiaryEntry(None, "")
    with pytest.raises(Exception) as e_contents:
        diary_entry_with_invalid_contents = DiaryEntry("", None)
    assert str(e_title.value) == "`title` argument was not a string."
    assert str(e_contents.value) == "`contents` argument was not a string."

# def test_format_returns_correctly_formatted_diary_entry():
#     diary_entry = DiaryEntry("My Day", "Today was a good day")
#     result = diary_entry.format()
#     assert result == "My Day:\nToday was a good day"

# def test_format_returns_formatted_entry_with_correct_placeholders():
#     diary_entries = [
#         DiaryEntry("", "Some contents"),
#         DiaryEntry("Some title", ""),
#         DiaryEntry("", ""),
#     ]
#     actual_formatted_entries = [
#         diary_entry.format()
#         for diary_entry in diary_entries
#     ]
#     expected_formatted_entries = [
#         "(Untitled entry)\nSome contents",
#         "Some title (Entry contents empty)",
#         "(Untitled entry, contents empty)",
#     ]
#     for actual, expected in zip(
#         actual_formatted_entries,
#         expected_formatted_entries
#     ):
#         assert actual == expected

def test_word_count_is_zero_if_diary_entry_contents_empty():
    diary_entry = DiaryEntry("", "")
    word_count = diary_entry.count_words()
    assert word_count == 0

def test_word_count_of_diary_entry_contents_correct():
    contents = "The quick brown fox jumped over the lazy dog."
    diary_entry = DiaryEntry("", contents)
    word_count = diary_entry.count_words()
    assert word_count == 9

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

def test_estimated_reading_time_is_zero_minutes_for_empty_contents():
    diary_entry = DiaryEntry("My title", "")
    estimated = diary_entry.reading_time(1)
    assert estimated == 0

def test_esimating_reading_time_with_invalid_wpm_raises_error():
    diary_entry = DiaryEntry("Title", "Some contents")
    with pytest.raises(Exception) as e_wpm_zero:
        diary_entry.reading_time(0)
    with pytest.raises(Exception) as e_wpm_negative:
        diary_entry.reading_time(-1)
    with pytest.raises(Exception) as e_wpm_non_integer:
        diary_entry.reading_time(None)
    for e in (e_wpm_zero, e_wpm_negative, e_wpm_non_integer):
        assert str(e.value) == "`wpm` argument was not a positive integer."

def test_estimated_reading_time_rounded_up_to_nearest_minute():
    diary_entry_1 = DiaryEntry("My title", "hello")
    estimated_1 = diary_entry_1.reading_time(10000)
    diary_entry_2 = DiaryEntry("My title", "a b c d e; f g h i j;")
    estimated_2 = diary_entry_2.reading_time(5)
    assert estimated_1 == 1
    assert estimated_2 == 2

def test_reading_chunk_always_empty_if_diary_entry_contents_empty():
    diary_entry = DiaryEntry("My title", "")
    chunks = [
        diary_entry.reading_chunk(1, 0),
        diary_entry.reading_chunk(1, 1),
        diary_entry.reading_chunk(1, 10),
    ]
    for chunk in chunks:
        assert chunk == ""

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
    for chunk in chunks:
        assert chunk == ""

def test_requesting_reading_chunk_with_invalid_wpm_raises_error():
    diary_entry = DiaryEntry("Title", "Some contents")
    with pytest.raises(Exception) as e_wpm_zero:
        diary_entry.reading_chunk(0, 1)
    with pytest.raises(Exception) as e_wpm_negative:
        diary_entry.reading_chunk(-1, 1)
    with pytest.raises(Exception) as e_wpm_non_integer:
        diary_entry.reading_chunk(None, 1)
    for e in (e_wpm_zero, e_wpm_negative, e_wpm_non_integer):
        assert str(e.value) == "`wpm` argument was not a positive integer."

def test_requesting_reading_chunk_with_invalid_minutes_raises_error():
    diary_entry = DiaryEntry("Title", "Some contents")
    with pytest.raises(Exception) as e_minutes_negative:
        diary_entry.reading_chunk(10, -1)
    with pytest.raises(Exception) as e_minutes_non_integer:
        diary_entry.reading_chunk(10, None)
    for e in (e_minutes_negative, e_minutes_non_integer):
        assert str(e.value) == "`minutes` argument was not a non-negative integer."

# def test_whitespace_character_sequences_in_contents_replaced_by_single_spaces_in_chunks():
#     unnormalised_contents = "One Two  Three\nFour\t\t\tFive \n \tSix  "
#     normalised_contents = convert_to_single_space_joined_words(unnormalised_contents)
#     diary_entry = DiaryEntry("", unnormalised_contents)
#     chunk = diary_entry.reading_chunk(2, 3)
#     assert chunk == normalised_contents

def test_requesting_reading_chunk_encompassing_all_contents_always_returns_all_words_joined_by_spaces():
    contents = "This entry contains\na total       of eight words."
    normalised_contents = convert_to_single_space_joined_words(contents)
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
    for chunk in chunks:
        assert chunk == normalised_contents

def test_repeated_reading_chunk_requests_return_successive_chunks_with_correct_restarts():
    contents = " This is a longer diary entry\n   containing a total of twelve words. "
    diary_entry = DiaryEntry("", contents)
    chunks = []
    for __ in range(4):
        chunks.append(diary_entry.reading_chunk(5, 1))
    assert chunks == [
        "This is a longer diary",
        "entry containing a total of",
        "twelve words.",
        "This is a longer diary"
    ]

def test_repeated_reading_chunk_requests_restart_correctly_and_do_not_return_empty_chunk():
    contents = "\n\nThis is a six \t word entry.\n\n"
    diary_entry = DiaryEntry("", contents)
    chunks = []
    for __ in range(3):
        chunks.append(diary_entry.reading_chunk(1, 3))
    assert chunks == [
        "This is a",
        "six word entry.",
        "This is a",
    ]
