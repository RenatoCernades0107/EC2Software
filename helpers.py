import math

def haversine(lat1, lon1, lat2, lon2):
    
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    # Radius of the Earth in kilometers
    radius = 6371
    
    # Calculate the distance
    distance = radius * c
    
    return distance

def menu() -> None:
    print(
        """
        API -> Utilizar API nominatim
        CSV -> Utilizar archivo CSV
        MOCK -> Utilizar Mock de Testing
        """
    )