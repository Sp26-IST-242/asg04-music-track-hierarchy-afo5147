"""
Represents a musical artist or podcast creator.

This is the simplest class in the hierarchy — no dependencies, no validation.
It introduces two core Python OOP conventions:
  1. The single leading-underscore (_name) signals a non-public attribute.
  2. @property exposes a clean public getter without allowing direct mutation.
"""
class Artist:
    def __init__(self, name, genre):
        self._name = name
        self._genre = genre

    @property
    def name(self):
        # this is to get the name of the artist
        return self._name

    @property
    def genre(self):
        # this is to get the genre of the artist
        return self._genre
    
    def __str__(self):
        # This is going to be the format for what is returned when printed
        return f"{self._name}, {self._genre}"