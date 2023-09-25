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