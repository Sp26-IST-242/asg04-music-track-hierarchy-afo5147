"""
A collection class that holds MusicTrack objects (Songs and Podcasts).

Design notes:
  • _tracks is kept private (single underscore) and exposed as a *copy*
    through the `tracks` property to protect encapsulation.
  • clear_playlist() uses list.clear() rather than rebinding to None or a new
    list, so the internal object reference stays valid.
  • sort_by_release_year() delegates to list.sort(), which in turn calls
    MusicTrack.__lt__ — the comparison logic defined in Part 3 pays off here.
  • __str__ uses a generator expression with str.join() for a concise
    multi-line string without building an intermediate list manually.
"""
from music_track import MusicTrack

class Playlist:
    '''
    This is going to manage all of the tracks in the playlist.
    '''
    def __init__(self):
        self._tracks = []

    def add_track(self, track: MusicTrack) -> None:
        # Add a track to the playlist.
        self._tracks.append(track)

    def clear_playlist(self) -> None:
        # Clear the playlist and getting rid of all the tracks.
        self._tracks.clear()

    def sort_by_release_year(self) -> None:
        # This is going to sort the tracks by release year.
        self._tracks.sort()

  
    @property
    def tracks(self) -> list[MusicTrack]:
        # This is going to get a copy of the trasks list.
        return list(self._tracks)
    

    def __str__(self):
        return "\n".join(str(track) for track in self._tracks)