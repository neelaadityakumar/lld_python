
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0.0

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        print(f"\n🌡️ Temperature updated to {temperature}°C")
        self._temperature = temperature
        self.notify()


class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"📱 Phone Display: Temperature is {temperature}°C")

class LEDDisplay(Observer):
    def update(self, temperature):
        print(f"💡 LED Display: Temperature is {temperature}°C")


station = WeatherStation()

phone = PhoneDisplay()
led = LEDDisplay()

station.attach(phone)
station.attach(led)

station.set_temperature(25.0)
station.set_temperature(30.5)

# Detach phone and update again
station.detach(phone)
station.set_temperature(28.2)

