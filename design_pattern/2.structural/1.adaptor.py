# You have a modern USB-C device, but only an old micro-USB charger —
#  you use an adapter in between so they work together.
from abc import ABC,abstractmethod
#Target class
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename: str):
        pass


class MP4Player:
    def play_mp4(self, filename):
        print(f"Playing MP4 file: {filename}")

class VLCPlayer:
    def play_vlc(self, filename):
        print(f"Playing VLC file: {filename}")


class MediaAdapter(MediaPlayer):
    def __init__(self, filetype: str):
        self.filetype = filetype.lower()
        if self.filetype == "mp4":
            self.advanced_player = MP4Player()
        elif self.filetype == "vlc":
            self.advanced_player = VLCPlayer()
        else:
            raise ValueError(f"Unsupported file type: {self.filetype}")

    def play(self, filename: str):
        if self.filetype == "mp4":
            self.advanced_player.play_mp4(filename)
        elif self.filetype == "vlc":
            self.advanced_player.play_vlc(filename)

class AudioPlayer(MediaPlayer):
    def play(self, filename: str):
        filetype = filename.split(".")[-1]

        if filetype == "mp3":
            print(f"Playing MP3 file: {filename}")
        elif filetype in ("mp4", "vlc"):
            adapter = MediaAdapter(filetype)
            adapter.play(filename)
        else:
            print(f"Unsupported file format: {filename}")


player = AudioPlayer()

player.play("rock.mp3")
player.play("movie.mp4")
player.play("live.vlc")
player.play("document.pdf")

