from lib.diary_entry import DiaryEntry

def test_can_create_instance_of_diary_entry():
    entry = DiaryEntry("", "")

def test_can_assign_title_and_contents_of_diary_entry():
    entry = DiaryEntry("My title", "Some contents")
    assert entry._title == "My title"
    assert entry._contents == "Some contents"