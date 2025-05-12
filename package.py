class Package:
    MAX_MASS = 20
    MAX_DIMENSION = 150
    MAX_VOLUME = 1000000

    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

    def __init__(self, length: int, width: int, height: int, mass: int):
        assert(length, int)
        assert(width, int)
        assert(height, int)
        assert(mass, int)
        
        self.dimensions = Dimensions(length, width, height)
        self.mass = mass
    
    def is_heavy(self) -> bool:
        return self.mass >= self.MAX_MASS

    def is_bulky(self) -> bool:
        return self.dimensions.get_volume() >= self.MAX_VOLUME or self.dimensions.get_largest_dimension() >= self.MAX_DIMENSION

    def get_stack_name(self):
        is_heavy = self.is_heavy()
        is_bulky = self.is_bulky()
        
        if is_heavy and is_bulky:
            return self.REJECTED
        elif is_heavy or is_bulky:
            return self.SPECIAL
        else:
            return self.STANDARD
        

class Dimensions:

    def __init__(self, length: int, width: int, height: int):
        self.length = length
        self.width = width
        self.height = height

    def get_largest_dimension(self) -> int:
        return max(self.length, self.width, self.height)
    
    def get_volume(self) -> int:
        return self.length * self.width * self.height