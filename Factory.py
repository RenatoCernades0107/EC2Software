from ILatLon import *
from APILatLon import *
from CSVLatLon import *
from MockLatLon import *

class Factory:
    def obtenerServicio(self, service: str) -> ILatLon:
        if service == 'CSV':
            return CSVLatLon()

        elif service == 'API':
            return APILatLon()

        elif service == 'MOCK':
            return MockLatLon()