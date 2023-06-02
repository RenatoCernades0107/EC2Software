from ILatLon import *
import requests
from requests import Request

class APILatLon(ILatLon):
    def getLatLon(self, ciudad: str, pais: str) -> Tuple[float, float]:
        response: Request = requests.get(f"https://nominatim.openstreetmap.org/search?q={ciudad.lower()},{pais.lower()}&format=json")
        body: list = response.json()
        lat: float = float(body[0].get("lat"))
        lon: float = float(body[0].get("lon"))
        return lat, lon

if __name__ == "__main__":
    obj = APILatLon()
    print(obj.getLatLon("Lima", "Peru"))