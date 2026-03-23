"""
Represents a music album or podcast series, including the years it was active.

Key concepts to implement:
  • Input validation in __init__ (fail-fast with a clear ValueError).
  • Defensive copy on both input and output so external code cannot corrupt
    the internal years list.
  • A *derived* property (debut_year) that computes its value from stored data
    rather than keeping a second field in sync.
"""
class Album:
    
    def __init__(self, title: str, active: bool, years: list[int]):
        # This is going to make sure that the list is not empty.
        if not years:
            raise ValueError("Please make sure years list is not empty.")
        
        self._title = title
        self._active = active
        self._years = list(years) # This is going to make sure that only a copy is stored

    @property
    def title(self) -> str:
        return self._title

    @property
    def active(self) -> bool:
        return self._active

    @property
    def years(self) -> list[int]:
        return list(self._years)

    @property
    def debut_year(self) -> str:
        # This is going to take the minimum of the years list and make it the debut year.
        return self._years[0]

    def __str__(self):
        return f"{self._title} active = {self._active} debut year: {self.debut_year}"