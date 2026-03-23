"""
Driver script demonstrating the complete Music Track hierarchy.

Run:
    python main.py

Expected output
---------------
Before sorting:
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False

After sorting:
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
"""
from artist import Artist
from album import Album
from song import Song
from podcast import Podcast
from playlist import Playlist

if __name__ == "__main__":
    # These are the artist and podcasters
    kendrick = Artist("Kendrick Lamar", "Hip-Hop")
    alanis = Artist("Alanis Morissette", "Alternative")
    joe = Artist("Joe Rogan", "Comedy")
    sarah = Artist("Sarah Koenig", "Journalism")

    # These are the albums and podcasts
    damn = Album("DAMN.", True, [2017, 2018])
    jagged = Album("Jagged Little Pill", False, [1995, 1996])
    joe_experience = Album("The Joe Rogan Experience", True, [2009, 2010])
    serial = Album("Serial", False, [2014, 2015])

    # These are the songs and podcast episodes
    song1 = Song("HUMBLE.", kendrick, damn, 220)
    song2 = Song("Ironic", alanis, jagged, 245)
    podcast1 = Podcast("Episode 1", joe, joe_experience, 9000, is_explicit=True)
    podcast2 = Podcast("Episode 1", sarah, serial, 5400)

    # This will be the playlist
    p = Playlist()
    p.add_track(song1)
    p.add_track(song2)
    p.add_track(podcast1)
    p.add_track(podcast2)

    # before sorting
    print("Before sorting:")
    print(p)
    

    p.sort_by_release_year()


    # after sorting
    print("\nAfter sorting:")
    print(p)