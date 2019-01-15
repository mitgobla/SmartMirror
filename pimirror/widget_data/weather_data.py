import weather
from PyQt5 import QtCore, QtGui
from time import sleep
from itertools import cycle

class Forecast(QtCore.QObject):
    """Weather using Yahoo-API

    Arguments:
        unit {str} : Unit of temperature
        location {str} : Location for weather
    """


    current_lookup = QtCore.pyqtSignal(weather.objects.weather_obj.WeatherObject)

    def __init__(self, unit="c", location="London"):
        super().__init__()

        if unit.lower() == "c":
            self.unit_cycle = cycle(['c', 'f'])
        else:
            self.unit_cycle = cycle(['f', 'c'])
        self.unit = next(self.unit_cycle)

        self.location = location
        self.weather_forecast = weather.Weather(unit=self.unit)
        self.lookup = None

    def toggle_unit(self):
        self.unit = next(self.unit_cycle)
        self.weather_forecast = weather.Weather(unit=self.unit)
        self.lookup = self.weather_forecast.lookup_by_location(self.location)
        self.current_lookup.emit(self.lookup)

    @QtCore.pyqtSlot()
    def update_forecast(self):
        while True:
            try:
                self.lookup = self.weather_forecast.lookup_by_location(self.location)
                self.current_lookup.emit(self.lookup)
            except:
                pass
            sleep(900)

