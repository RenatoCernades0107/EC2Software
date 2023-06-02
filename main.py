from Factory import Factory
from helpers import *
from ILatLon import *


def main() -> None:
    factory: Factory = Factory()
    option: str = "@"
    while option:
        # Show menu
        menu()
        # Select service
        option: str = input("Elija una opción: ")
        service: ILatLon = factory.obtenerServicio(option)

        country: str = input("Nombre del primer país: ")
        city: str = input("Nombre de la primer ciudad: ")

        # Get latitud and longitud of the first location
        (lat, long) = service.getLatLon(country, city)

        country2: str = input("Nombre del segundo país: ")
        city2: str = input("Nombre de la segundo ciudad: ")

        # Get latitud and longitud of the second location
        (lat2, long2) = service.getLatLon(country2, city2)

        distance = haversine(lat, long, lat2, long2)

        print(f"La distancia desde ({city}, {country}) hasta ({city2}, {country2}) es {distance}")

main()
