class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigcap = big
        self.medcap = medium
        self.smacap = small

    def addCar(self, carType: int) -> bool:
        match carType:
            case 1:
                if not self.bigcap: return False
                self.bigcap -= 1
                return True
            case 2:
                if not self.medcap: return False
                self.medcap -= 1
                return True
            case 3:
                if not self.smacap: return False
                self.smacap -= 1
                return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)