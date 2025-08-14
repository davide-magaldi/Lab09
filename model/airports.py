from dataclasses import dataclass


@dataclass
class Airport:
    ID: int
    IATA_CODE: str
    AIRPORT: str
    CITY: str
    STATE: str
    COUNTRY: str
    LATITUDE: float
    LONGITUDE: float
    TIMEZONE_OFFSET: float

    def __init__(self, ID, IATA_CODE, AIRPORT, CITY, STATE, COUNTRY, LATITUDE, LONGITUDE, TIMEZONE_OFFSET):
        self.ID = ID
        self.IATA_CODE = IATA_CODE
        self.AIRPORT = AIRPORT
        self.CITY = CITY
        self.STATE = STATE
        self.COUNTRY = COUNTRY
        self.LATITUDE = LATITUDE
        self.LONGITUDE = LONGITUDE
        self.TIMEZONE_OFFSET = TIMEZONE_OFFSET

    def __hash__(self):
        return hash(self.ID)



