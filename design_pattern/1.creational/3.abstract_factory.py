
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class TextBox(ABC):
    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):
    def render(self):
        print("Rendering Windows Button")

class WindowsTextBox(TextBox):
    def render(self):
        print("Rendering Windows TextBox")



class MacButton(Button):
    def render(self):
        print("Rendering Mac Button")

class MacTextBox(TextBox):
    def render(self):
        print("Rendering Mac TextBox")


class WidgetFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_textbox(self) -> TextBox:
        pass


class WindowsFactory(WidgetFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_textbox(self) -> TextBox:
        return WindowsTextBox()

class MacFactory(WidgetFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_textbox(self) -> TextBox:
        return MacTextBox()


def render_ui(factory):
    button = factory.create_button()
    textbox = factory.create_textbox()
    button.render()
    textbox.render()


# Use Windows UI
win_factory = WindowsFactory()
render_ui(win_factory)

# Use Mac UI
mac_factory = MacFactory()
render_ui(mac_factory)

