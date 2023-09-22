# Music Journal Class Design Recipe

## 1. Problem description

> As a user  
> So that I can keep track of my music listening  
> I want to add tracks I've listened to and see a list of them.

## 2. Class interface

```python
class MusicJournal:
    # User-facing properties:
    #   Constants:
    #     `NON_STRING_TRACK_NAME_EXCEPTION_MSG`
    #     `ZERO_TRACK_NAMES_STORED_INFORMATIVE_MESSAGE`, string
    #     `DEFAULT_LISTING_HEADER_MESSAGE`, string

    def __init__(self):
        # Side effects:
        #   Create `_tracks_listened_to` attribute
        pass

    def add_track(self, track_name):
        # Parameters:
        #   `track_name`, string: the name of the track the user has listened to
        # Side effects:
        #   Add `track_name` to `self._tracks_listened_to`
        #   Raise an exception if `track_name` is not a string
        pass

    def get_listing_of_tracks(self):
        # Returns:
        #   string: a nicely formatted list of tracks the user has listened to,
        #           in no particular order
        #           OR a message informing the user no tracks have been added
        pass

```

## 3. Examples for testing

```python

"""
When the music journal module is imported
The music journal class constants have their correct values
"""
MusicJournal.NON_STRING_TRACK_NAME_EXCEPTION_MSG  # => correct value
MusicJournal.ZERO_TRACK_NAMES_STORED_INFORMATIVE_MESSAGE  # => correct value
MusicJournal.DEFAULT_LISTING_HEADER_MESSAGE  # => correct value

"""
When a new music journal instance is created
The attribute for storing tracks listened to is empty
"""
journal = MusicJournal()
journal._tracks_listened_to  # => (empty object)

"""
When we add a track to a new music journal
The track is stored as one of the tracks listened to
"""
journal = MusicJournal()
journal.add_track("Example track")
"Example track" in journal._tracks_listened_to  # => True

"""
When we add a track to a new music journal
The track is the only thing stored as one of the tracks listened to
"""
journal = MusicJournal()
journal.add_tracks("Example track")
len(journal._tracks_listened_to)  # => 1

"""
When we add two different tracks to a new music journal
The two tracks are stored as tracks listened to
"""
journal = MusicJournal()
journal.add_track("First")
journal.add_track("Second")
"First" in journal._tracks_listened_to\
    and "Second" in journal._tracks_listened_to  # => True

"""
When we add two different tracks to a new music journal
The two tracks are the only thing stored as tracks listened to
"""
journal = MusicJournal()
journal.add_track("First")
journal.add_track("Second")
len(journal._tracks_listened_to)  # => 2

"""
When we add the same track twice to a new music journal
The first time, the track is stored as a track listened to
The second time, nothing happens as the track is already stored
"""
journal = MusicJournal()
journal.add_track("So good it makes you listen twice")
journal.add_track("So good it makes you listen twice")
"So good it makes you listen twice" in journal._tracks_listened_to  # => True
len(journal._tracks_listened_to)  # => 1

"""
When we try to add a track
And provide a non-string value for `track_name`
It raises an exception
"""
journal = MusicJournal()
journal.add_track(None)  # raises an exception

"""
If no tracks have been added yet
When we get a listing of tracks
It returns a message informing us no tracks have been listened to
"""
journal = MusicJournal()
journal.get_listing_of_tracks()  # => string containing an informative message

"""
If one track has been added
When we get a listing of tracks
It returns a correctly formatted listing containing just that track
"""
journal = MusicJournal()
journal.add_track("First!")
journal.get_listing_of_tracks()   # => "You've listened to these tracks:\n  * First!"

"""
If two different tracks have been added
When we get a list of tracks
It returns a correctly formatted listing containing just those tracks, in either order
"""
journal = MusicJournal()
journal.add_track("Hello")
journal.add_track("World")
journal.get_listing_of_tracks()  # => correctly formatted listing in either order

"""
If multiple tracks have been added
When we get a list of tracks
It returns a correctly formatted listing containing just those tracks, in any order
"""
journal = MusicJournal()
track_names = [
    "a", "b", "c", "d", "e",
]
for track_name in track_names:
    journal.add_track(track_name)
lines = journal.get_listing_of_tracks().split("\n")
lines[0]  # => "You've listened to these tracks:"
set(lines[1:])  # => set("  * " + track_name for track_name in track_names)

```

## 4. Implementation

The implementation of the class is found in `./lib/music_journal.py`.

The implementation of the tests is found in `./tests/test_music_journal.py`.
