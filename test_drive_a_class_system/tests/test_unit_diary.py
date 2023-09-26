import pytest
from lib.diary import Diary

def test_can_create_instance_of_diary():
    diary = Diary()

def test_all_method_returns_empty_list_for_new_diary():
    diary = Diary()
    result = diary.all()
    assert result == []

def test_count_words_method_returns_0_for_new_diary():
    diary = Diary()
    result = diary.count_words()
    assert result == 0

def test_estimated_total_reading_time_is_zero_minutes_for_new_diary():
    diary = Diary()
    estimated = diary.reading_time(1)
    assert estimated == 0

def test_estimating_total_reading_time_with_invalid_wpm_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e_wpm_zero:
        diary.reading_time(0)
    with pytest.raises(Exception) as e_wpm_negative:
        diary.reading_time(-1)
    with pytest.raises(Exception) as e_wpm_non_integer:
        diary.reading_time(None)
    for e in (e_wpm_zero, e_wpm_negative, e_wpm_non_integer):
        assert str(e.value) == "`wpm` argument was not a positive integer."

def test_finding_best_entry_for_reading_time_with_invalid_wpm_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e_wpm_zero:
        diary.find_best_entry_for_reading_time(0, 1)
    with pytest.raises(Exception) as e_wpm_negative:
        diary.find_best_entry_for_reading_time(-1, 1)
    with pytest.raises(Exception) as e_wpm_non_integer:
        diary.find_best_entry_for_reading_time(None, 1)
    for e in (e_wpm_zero, e_wpm_negative, e_wpm_non_integer):
        assert str(e.value) == "`wpm` argument was not a positive integer."

def test_finding_best_entry_for_reading_time_with_invalid_minutes_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e_minutes_negative:
        diary.find_best_entry_for_reading_time(10, -1)
    with pytest.raises(Exception) as e_minutes_non_integer:
        diary.find_best_entry_for_reading_time(10, None)
    for e in (e_minutes_negative, e_minutes_non_integer):
        assert str(e.value) == "`minutes` argument was not a non-negative integer."

def test_find_best_entry_for_reading_time_returns_none_for_new_diary():
    diary = Diary()
    result = diary.find_best_entry_for_reading_time(1, 1)
    assert result is None
