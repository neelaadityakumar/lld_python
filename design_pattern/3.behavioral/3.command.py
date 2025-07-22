# The Command Pattern turns a request into a stand-alone object (called a command)
# that contains all information about the action to be performed — making actions decoupled from the invoker.

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

class RemoteControl:
    def __init__(self):
        self.history = []

    def submit(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
        else:
            print("No commands to undo.")


# Receivers
light = Light()

# Commands
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

# Invoker
remote = RemoteControl()

remote.submit(light_on)
remote.submit(light_off)

print("\nUndoing last two commands:")
remote.undo_last()
remote.undo_last()

