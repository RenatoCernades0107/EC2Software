from typing import Tuple
from ILatLon import *

class MockLatLon(ILatLon):
    def getLatLon(self, ciudad: str, pais: str) -> Tuple[float, float]:
        return 123456789, 987654321
    
if __name__ == "__main__":
    obj = MockLatLon()
    print(obj.getLatLon("Lima", "Peru"))