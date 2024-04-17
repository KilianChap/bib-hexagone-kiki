class WeatherData:
    def __init__(self):
        self.temperatureDisplay = 0
        self.humidityDisplay = 0
        self.pressureDisplay = 0

    def getTemperature(self):
        return self.temperatureDisplay

    def getHumidity(self):
        return self.humidityDisplay

    def getPressure(self):
        return self.pressureDisplay

    def measurementsChanged(self, temperature, humidity, pressure):
        self.temperatureDisplay = temperature
        self.humidityDisplay = humidity
        self.pressureDisplay = pressure
        self.notifyObservers()

    def notifyObservers(self):
        # In a real-world scenario, you would notify all registered observers.
        # For simplicity, we assume that there are specific instances of observer classes.
        temp_display.update(self.temperatureDisplay)
        humidity_display.update(self.humidityDisplay)
        pressure_display.update(self.pressureDisplay)


class TempDisplay:
    def update(self, temperature):
        print("Temperature sensor updated:", temperature)


class PressureDisplay:
    def update(self, pascal):
        print("Pressure sensor updated:", pascal)


class HumidityDisplay:
    def update(self, humidity_percentage):
        print("Humidity sensor updated:", humidity_percentage)


# Example usage:
weather_station = WeatherData()
temp_display = TempDisplay()
pressure_display = PressureDisplay()
humidity_display = HumidityDisplay()

weather_station.measurementsChanged(25, 50, 1013)