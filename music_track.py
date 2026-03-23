"""
Abstract base class for all music tracks (Songs and Podcasts).

Design decisions to implement:
  • ABC makes it impossible to instantiate MusicTrack directly — you can only
    create concrete subclasses that implement every @abstractmethod.
  • Common fields (artist, album, duration_seconds) live here so that Song and
    Podcast do not each need to repeat them.
  • release_year is a *derived* property delegating to Album.debut_year; the
    year is not stored a second time.
  • play_time_formatted() is abstract because Song and Podcast format time
    differently (MM:SS vs HH:MM:SS).
  • total_play_time() is concrete because the calculation is identical for all
    track types: duration × number of plays.
  • @functools.total_ordering generates <=, >, >= automatically from __eq__ and
    __lt__, giving us full comparison support with minimal code.
  • __hash__ is defined to stay consistent with __eq__ (Python sets __hash__ to
    None when you define __eq__, making objects unhashable unless you fix it).
"""
from abc import ABC, abstractmethod
from artist import Artist
from album import Album
from functools import total_ordering

@total_ordering
class MusicTrack(ABC):
    def __init__(self, artist: Artist, album: Album, duration_seconds: float):
        self._artist = artist
        self._album = album
        self._duration_seconds = duration_seconds
      
    @property
    def artist(self) -> Artist:
        return self._artist

    @property
    def album(self) -> Album:
        return self._album

    @property
    def duration_seconds(self) -> float:
        return self._duration_seconds

    @property
    def release_year(self) -> int:
        return self.album.debut_year



    @abstractmethod
    def play_time_formatted(self) -> str:
        pass

    def total_play_time(self, num_plays: int) -> float:
        return float(self.duration_seconds * num_plays)



    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MusicTrack):
            return False
        return self.release_year == other.release_year

    def __lt__(self, other: object) -> bool:
        # This is going to determin the order of the tracks.
        if not isinstance(other, MusicTrack):
            return False
        return self.release_year < other.release_year

    def __hash__(self) -> int:
        return hash(self.release_year)
