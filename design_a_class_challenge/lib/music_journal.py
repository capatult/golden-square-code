class MusicJournal:
    NON_STRING_TRACK_NAME_EXCEPTION_MESSAGE = "`track_name` was not a string."
    ZERO_TRACK_NAMES_STORED_INFORMATIVE_MESSAGE = "You haven't added any tracks yet."
    DEFAULT_LISTING_HEADER_MESSAGE = "You've listened to these tracks:"

    def __init__(self):
        self._tracks_listened_to = set()

    def add_track(self, track_name):
        if not isinstance(track_name, str):
            raise Exception(self.NON_STRING_TRACK_NAME_EXCEPTION_MESSAGE)
        self._tracks_listened_to.add(track_name)

    def get_listing_of_tracks(self):
        if len(self._tracks_listened_to) == 0:
            return self.ZERO_TRACK_NAMES_STORED_INFORMATIVE_MESSAGE
        unformatted_lines = [self.DEFAULT_LISTING_HEADER_MESSAGE]
        unformatted_lines.extend(self._tracks_listened_to)
        return "\n  * ".join(unformatted_lines)