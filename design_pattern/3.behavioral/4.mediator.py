# The Mediator Pattern defines an object that centralizes communication
# between components (colleagues), so they don’t refer to each other directly.


class ChatRoom:
    def show_message(self, sender: str, message: str):
        print(f"[{sender}]: {message}")


class User:
    def __init__(self, name: str, chatroom: ChatRoom):
        self.name = name
        self.chatroom = chatroom

    def send(self, message: str):
        self.chatroom.show_message(self.name, message)


room = ChatRoom()

aditya = User("Aditya", room)
john = User("John", room)

aditya.send("Hi, John!")
john.send("Hey Aditya, how's it going?")

