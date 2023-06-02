from ILatLon import *

class CSVLatLon(ILatLon):
    def getLatLon(self, ciudad: str, pais: str) -> Tuple[float, float]:
        file = open("worldcities.csv", encoding="utf8")
        line = file.readline()
        while True:
            line = file.readline()
            if not line:
                raise Exception("No city and country found")
            values = line.split(",")
            if values[1][1:-1] == ciudad and values[4][1:-1] == pais:
                return (float(values[2][1:-1]), float(values[3][1:-1]))


if __name__ == "__main__":
    obj = CSVLatLon()
    print(obj.getLatLon("Lima", "Peru"))
