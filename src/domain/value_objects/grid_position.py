from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class GridPosition:
    """A value object representing a position in the hexagonal grid.
    
    This is an immutable value object that represents a position in the grid
    using axial coordinates (q, r) system for hexagonal grids.
    
    Attributes:
        q (int): The q-coordinate in the axial coordinate system (column)
        r (int): The r-coordinate in the axial coordinate system (row)
    """
    q: int
    r: int
    
    def as_tuple(self) -> Tuple[int, int]:
        """Convert the position to a tuple representation.
        
        Returns:
            Tuple[int, int]: A tuple of (q, r) coordinates
        """
        return (self.q, self.r)
    
    def __str__(self) -> str:
        return f"GridPosition(q={self.q}, r={self.r})" 