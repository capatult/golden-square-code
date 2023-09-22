import pytest
from lib.music_journal import *
MusicJournal = MusicJournal  # helps with pylance linter

"""
When the music journal module is imported
The music journal class constants have their correct values
"""
def test_music_journal_class_has_correct_constant_properties():
    assert (
        MusicJournal.NON_STRING_TRACK_NAME_EXCEPTION_MESSAGE,
        MusicJournal.ZERO_TRACK_NAMES_STORED_INFORMATIVE_MESSAGE,
        MusicJournal.DEFAULT_LISTING_HEADER_MESSAGE,
    ) == (
        "`track_name` was not a string.",
        "You haven't added any tracks yet.",
        "You've listened to these tracks:",
    )

"""
When a new music journal instance is created
The attribute for storing tracks listened to is empty
"""
def test_new_music_journal_has_empty_tracks_listened_to_attribute():
    journal = MusicJournal()
    assert journal._tracks_listened_to == set()

"""
When we add a track to a new music journal
The track is stored as one of the tracks listened to
"""
def test_adding_new_track_to_new_music_journal_stores_that_track():
    journal = MusicJournal()
    journal.add_track("Example track")
    assert "Example track" in journal._tracks_listened_to

"""
When we add a track to a new music journal
The track is the only thing stored as one of the tracks listened to
"""
def test_adding_new_track_to_new_music_journal_adds_only_1_track():
    journal = MusicJournal()
    journal.add_track("Example track")
    assert len(journal._tracks_listened_to) == 1


"""
When we add two different tracks to a new music journal
The two tracks are both stored as tracks listened to
"""
def test_adding_2_new_tracks_to_new_music_journal_stores_both_tracks():
    journal = MusicJournal()
    journal.add_track("First")
    journal.add_track("Second")
    assert "First" in journal._tracks_listened_to
    assert "Second" in journal._tracks_listened_to


"""
When we add two different tracks to a new music journal
The two tracks are the only thing stored as tracks listened to
"""
def test_adding_2_new_tracks_to_new_music_journal_adds_only_2_tracks():
    journal = MusicJournal()
    journal.add_track("First")
    journal.add_track("Second")
    assert len(journal._tracks_listened_to) == 2

"""
When we add the same track twice to a new music journal
The first time, the track is stored as a track listened to
The second time, nothing happens as the track is already stored
"""
def test_adding_already_present_track_to_music_journal_does_nothing():
    journal = MusicJournal()
    track_name = "So good it makes you listen twice"
    for __ in range(2):
        journal.add_track(track_name)
    assert track_name in journal._tracks_listened_to
    assert len(journal._tracks_listened_to) == 1

"""
When we try to add a track
And provide a non-string value for `track_name`
It raises an exception
"""
def test_attempting_to_add_non_string_track_name_raises_exception():
    journal = MusicJournal()
    non_string_objects = [
        None, 0, False, True, 42, 3.141, list(),
    ]
    error_messages = []
    for non_string_object in non_string_objects:
        with pytest.raises(Exception) as e:
            journal.add_track(non_string_object)
        error_messages.append(str(e.value))
    for error_message in error_messages:
        assert error_message == journal.NON_STRING_TRACK_NAME_EXCEPTION_MESSAGE

"""
If no tracks have been added yet
When we get a listing of tracks
It returns a message informing us no tracks have been listened to
"""
def test_get_listing_of_tracks_returns_correct_message_if_0_track_names_stored():
    journal = MusicJournal()
    listing = journal.get_listing_of_tracks()
    assert listing == journal.ZERO_TRACK_NAMES_STORED_INFORMATIVE_MESSAGE

"""
If one track has been added
When we get a listing of tracks
It returns a correctly formatted listing containing just that track
"""
def test_get_listing_of_tracks_returns_the_valid_1_track_listing_if_1_track_stored():
    journal = MusicJournal()
    journal.add_track("First!")
    listing = journal.get_listing_of_tracks()
    assert listing == f"{journal.DEFAULT_LISTING_HEADER_MESSAGE}\n  * First!"

"""
If two different tracks have been added
When we get a list of tracks
It returns a correctly formatted listing containing just those tracks, in either order
"""
def test_get_listing_of_tracks_returns_any_valid_2_track_listing_if_2_tracks_stored():
    journal = MusicJournal()
    journal.add_track("Hello")
    journal.add_track("World")
    listing = journal.get_listing_of_tracks()
    assert listing in (
        f"{journal.DEFAULT_LISTING_HEADER_MESSAGE}\n  * Hello\n  * World",
        f"{journal.DEFAULT_LISTING_HEADER_MESSAGE}\n  * World\n  * Hello",
    )

"""
If multiple tracks have been added
When we get a list of tracks
It returns a correctly formatted listing containing just those tracks, in any order
"""
def test_get_listing_of_tracks_returns_any_valid_5_track_listing_if_5_tracks_stored():
    journal = MusicJournal()
    track_names = [
        "a", "b", "c", "d", "e",
    ]
    for track_name in track_names:
        journal.add_track(track_name)
    lines = journal.get_listing_of_tracks().split("\n")
    assert lines[0] == journal.DEFAULT_LISTING_HEADER_MESSAGE
    assert set(lines[1:]) == set(
        f"  * {track_name}" for track_name in track_names
    )







