from ILatLon import *
import csv


class CSVLatLon(ILatLon):
    def getLatLon(self, ciudad: str, pais: str) -> Tuple[float, float]:
        with csv.reader("worldcities.csv") as reader:
            line = file.readline()
            while True:
                line = file.readline()
                if not line:
                    break
                values = line.split(",")
                if values[1] == ciudad and values[4] == pais:
                    return (float(values[2]), float(values[3]))


if __name__ == "__main__":
    obj = CSVLatLon()
    print(obj.getLatLon("Lima", "Peru"))
