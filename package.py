class Package:
    MAX_WEIGHT = 20
    MAX_DIMENSION = 150
    MAX_VOLUME = 1000000

    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

    def __init__(self, length: int, width: int, height: int, weight: int):
        self.dimensions = Dimensions(length, width, height)
        self.weight = weight
    
    def is_heavy(self) -> bool:
        return self.weight >= self.MAX_WEIGHT

    def is_bulky(self) -> bool:
        return Dimensions.get_volume() >= self.MAX_VOLUME or Dimensions.get_largest_dimension() >= self.MAX_DIMENSION

    def get_stack_name(self):
        is_heavy = is_heavy()
        is_bulky = is_bulky()
        
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