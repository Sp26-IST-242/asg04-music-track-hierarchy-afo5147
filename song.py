"""
Concrete subclass of MusicTrack representing a standard music track.

Song adds no new fields beyond what MusicTrack already stores.  Its only
responsibility is to:
  1. Call super().__init__() to let MusicTrack do the storage work.
  2. Implement play_time_formatted() in MM:SS format.
     Return the duration as 'MM:SS' (both parts zero-padded).

        Examples
        --------
        220 seconds → '03:40'
        65  seconds → '01:05'
        
  3. Override __str__ for a human-readable representation.
     Return '(<artist>) <album>, duration: <MM:SS>'.

        Example:
            (Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017,
            duration: 03:40
"""
from music_track import MusicTrack

class Song(MusicTrack):
    '''
    This is going to be the concrete subclass for the music track.
    '''
    def __init__(self, artist, album, duration_seconds):
        super().__init__(artist, album, duration_seconds)

    def play_time_formatted(self) -> str:
        minutes = int(self.duration_seconds // 60)
        seconds = int(self.duration_seconds % 60)
        return f"{minutes:02}:{seconds:02}"

    def __str__(self):
        return f"({self.artist}) {self.album}, duration: {self.play_time_formatted()}"