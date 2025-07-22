# The Bridge Pattern decouples an abstraction from its implementation so that the two can vary independently.
# Imagine a TV remote:

# - The remote is the abstraction
# - The TV (Sony, Samsung, etc.) is the implementation

# You should be able to use any remote with any TV, without hardcoding the combinations.

from abc import ABC, abstractmethod

class TV(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def tune_channel(self, channel: int):
        pass


class SonyTV(TV):
    def on(self):
        print("Sony TV: Power ON")

    def off(self):
        print("Sony TV: Power OFF")

    def tune_channel(self, channel: int):
        print(f"Sony TV: Tuning to channel {channel}")

class SamsungTV(TV):
    def on(self):
        print("Samsung TV: Power ON")

    def off(self):
        print("Samsung TV: Power OFF")

    def tune_channel(self, channel: int):
        print(f"Samsung TV: Switching to channel {channel}")


class RemoteControl:
    def __init__(self, tv: TV):
        self._tv = tv

    def turn_on(self):
        self._tv.on()

    def turn_off(self):
        self._tv.off()

    def set_channel(self, channel: int):
        self._tv.tune_channel(channel)



sony = SonyTV()
samsung = SamsungTV()

remote1 = RemoteControl(sony)
remote1.turn_on()
remote1.set_channel(5)
remote1.turn_off()

print()

remote2 = RemoteControl(samsung)
remote2.turn_on()
remote2.set_channel(9)
remote2.turn_off()


