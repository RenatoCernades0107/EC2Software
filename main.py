from Factory import Factory
from helpers import *
from ILatLon import *


def main() -> None:
    factory: Factory = Factory()
    option: str = ""
    while True:
        # Show menu
        menu()
        # Select service
        option: str = input("Elija una opción o X para salir: ")
        if option not in ["CSV", "MOCK", "API", "X"]:
            continue
        if option == "X":
            break
        service: ILatLon = factory.obtenerServicio(option)

        country: str = input("Nombre del primer país: ")
        city: str = input("Nombre de la primer ciudad: ")

        # Get latitud and longitud of the first location
        (lat, long) = service.getLatLon(ciudad=city, pais=country)

        country2: str = input("Nombre del segundo país: ")
        city2: str = input("Nombre de la segundo ciudad: ")

        # Get latitud and longitud of the second location
        (lat2, long2) = service.getLatLon(ciudad=city2, pais=country2)

        distance = haversine(lat, long, lat2, long2)

        print(f"La distancia desde ({city}, {country}) hasta ({city2}, {country2}) es {distance} kilómetros")

main()
