# > The Facade Pattern provides a unified, simplified interface to a complex system of classes, libraries, or APIs.

# Think of a **hotel concierge**:

# - You don’t deal with housekeeping, room service, or maintenance separately.
# - You call **one number**, and the concierge manages everything behind the scenes.

class Projector:
    def on(self):
        print("Projector: Turning on")

    def off(self):
        print("Projector: Shutting down")

    def set_input(self, source: str):
        print(f"Projector: Setting input to {source}")


class SpeakerSystem:
    def on(self):
        print("Speakers: Powering on")

    def off(self):
        print("Speakers: Powering down")

    def set_volume(self, level: int):
        print(f"Speakers: Volume set to {level}")


class StreamingService:
    def connect(self):
        print("Streaming Service: Connecting to Netflix...")

    def disconnect(self):
        print("Streaming Service: Disconnecting")

    def play_movie(self, title: str):
        print(f"Streaming Service: Playing '{title}'")


class HomeTheaterFacade:
    def __init__(self):
        self.projector = Projector()
        self.speakers = SpeakerSystem()
        self.streaming = StreamingService()

    def start_movie(self, title: str):
        print("\n--- Starting Movie Setup ---")
        self.projector.on()
        self.projector.set_input("HDMI 1")
        self.speakers.on()
        self.speakers.set_volume(15)
        self.streaming.connect()
        self.streaming.play_movie(title)
        print("--- Movie Started ---\n")

    def end_movie(self):
        print("\n--- Shutting Down Movie ---")
        self.streaming.disconnect()
        self.speakers.off()
        self.projector.off()
        print("--- System Shutdown Complete ---\n")

home_theater = HomeTheaterFacade()
home_theater.start_movie("Interstellar")
home_theater.end_movie()