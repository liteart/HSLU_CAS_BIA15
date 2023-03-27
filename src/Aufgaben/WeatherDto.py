from typing import Optional


class WeatherDto:
    COL_SEPARATOR = ";"

    __coord_lon: float = 0.0
    __coord_lat: float = 0.0
    __weather_id: int = -1
    __weather_main: Optional[str] = None
    __weather_icon: Optional[str] = None
    __main_temp: float = 0.0
    __main_feels_like: float = 0.0
    __main_temp_min: float = 0.0
    __main_temp_max: float = 0.0
    __main_pressure: int = 0
    __main_humidity: int = 0
    __wind_speed: float = 0.0
    __wind_deg: float = 0.0
    __clouds_all: int = 20
    __id: int = -1
    __name: Optional[str] = None

    @property
    def coord_lon(self):
        return self.__coord_lon

    @coord_lon.setter
    def coord_lon(self, value):
        self.__coord_lon = value

    @property
    def coord_lat(self):
        return self.__coord_lat

    @coord_lat.setter
    def coord_lat(self, value):
        self.__coord_lat = value

    @property
    def weather_id(self):
        return self.__weather_id

    @weather_id.setter
    def weather_id(self, value):
        self.__weather_id = value

    @property
    def weather_main(self):
        return self.__weather_main

    @weather_main.setter
    def weather_main(self, value):
        self.__weather_main = value

    @property
    def weather_icon(self):
        return self.__weather_icon

    @weather_icon.setter
    def weather_icon(self, value):
        self.__weather_icon = value

    @property
    def main_temp(self):
        return self.__main_temp

    @main_temp.setter
    def main_temp(self, value):
        self.__main_temp = value

    @property
    def main_feels_like(self):
        return self.__main_feels_like

    @main_feels_like.setter
    def main_feels_like(self, value):
        self.__main_feels_like = value

    @property
    def main_temp_min(self):
        return self.__main_temp_min

    @main_temp_min.setter
    def main_temp_min(self, value):
        self.__main_temp_min = value

    @property
    def main_temp_max(self):
        return self.__main_temp_max

    @main_temp_max.setter
    def main_temp_max(self, value):
        self.__main_temp_max = value

    @property
    def main_pressure(self):
        return self.__main_pressure

    @main_pressure.setter
    def main_pressure(self, value):
        self.__main_pressure = value

    @property
    def main_humidity(self):
        return self.__main_humidity

    @main_humidity.setter
    def main_humidity(self, value):
        self.__main_humidity = value

    @property
    def wind_speed(self):
        return self.__wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        self.__wind_speed = value

    @property
    def wind_deg(self):
        return self.__wind_deg

    @wind_deg.setter
    def wind_deg(self, value):
        self.__wind_deg = value

    @property
    def clouds_all(self):
        return self.__clouds_all

    @clouds_all.setter
    def clouds_all(self, value):
        self.__clouds_all = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @staticmethod
    def from_json(obj: any):
        instance = WeatherDto()
        instance.coord_lon = obj["coord"]["lon"]
        instance.coord_lat = obj["coord"]["lat"]
        instance.weather_id = obj["weather"][0]["id"]
        instance.weather_main = obj["weather"][0]["main"]
        instance.weather_icon = obj["weather"][0]["icon"]
        instance.main_temp = obj["main"]["temp"]
        instance.main_feels_like = obj["main"]["feels_like"]
        instance.main_temp_min = obj["main"]["temp_min"]
        instance.main_temp_max = obj["main"]["temp_max"]
        instance.main_pressure = obj["main"]["pressure"]
        instance.main_humidity = obj["main"]["humidity"]
        instance.wind_speed = obj["wind"]["speed"]
        instance.wind_deg = obj["wind"]["deg"]
        instance.clouds_all = obj["clouds"]["all"]
        instance.id = obj["id"]
        instance.name = obj["name"]

        return instance

    def to_csv(self) -> str:
        return str(self.coord_lon) + self.COL_SEPARATOR \
            + str(self.coord_lat) + self.COL_SEPARATOR \
            + str(self.weather_id) + self.COL_SEPARATOR \
            + self.weather_main + self.COL_SEPARATOR \
            + self.weather_icon + self.COL_SEPARATOR \
            + str(self.main_temp) + self.COL_SEPARATOR \
            + str(self.main_feels_like) + self.COL_SEPARATOR \
            + str(self.main_temp_min) + self.COL_SEPARATOR \
            + str(self.main_temp_max) + self.COL_SEPARATOR \
            + str(self.main_pressure) + self.COL_SEPARATOR \
            + str(self.main_humidity) + self.COL_SEPARATOR \
            + str(self.wind_speed) + self.COL_SEPARATOR \
            + str(self.wind_deg) + self.COL_SEPARATOR \
            + str(self.clouds_all) + self.COL_SEPARATOR \
            + str(self.id) + self.COL_SEPARATOR \
            + self.name

    def to_flat_obj(self) -> dict:
        return {
            'coord_lon': [self.coord_lon],
            'coord_lat': [self.coord_lat],
            'weather_id': [self.weather_id],
            'weather_main': [self.weather_main],
            'weather_icon': [self.weather_icon],
            'main_temp': [self.main_temp],
            'main_feels_like': [self.main_feels_like],
            'main_temp_min': [self.main_temp_min],
            'main_temp_max': [self.main_temp_max],
            'main_pressure': [self.main_pressure],
            'main_humidity': [self.main_humidity],
            'wind_speed': [self.wind_speed],
            'wind_deg': [self.wind_deg],
            'clouds_all': [self.clouds_all],
            'id': [self.id],
            'name': [self.name]
        }
